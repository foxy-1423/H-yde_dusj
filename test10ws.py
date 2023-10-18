import serial
import asyncio
import websockets

# Define the COM port and baud rate
com_port = 'COM3'  # Replace with your COM port name
baud_rate = 9600  # Adjust to match your sensor's baud rate

# Define the WebSocket server URL
websocket_server_url = "localhost"  # Replace with the WebSocket server URL
websocket_server_port = 8765  # Replace with the WebSocket server port

async def read_and_send_data(ser, websocket, path):
    try:
        while True:
            # Read data from the COM port until a carriage return character is encountered
            data = await asyncio.get_event_loop().run_in_executor(None, ser.read, 10)
            while True:
                char = ser.read(1)
                data += char
                if char == b'\r':
                    break
            
            # Process the data if it's not empty and ends with a carriage return
            if data and data.endswith(b'\r'):
                # Extract the last 4 characters as the distance value
                distance_str = data[-5:-1].decode('utf-8')

                    # Convert the distance value to an integer
                try:
                        distance = int(distance_str)
                        print(f"Distance: {distance} units")

                        # Send the distance data to all connected WebSocket clients
                        await websocket.send(distance_str)
                except ValueError:
                        print("Invalid distance data received")
    except KeyboardInterrupt:
        pass

async def main():
    # Initialize the serial connection
    ser = serial.Serial(com_port, baud_rate)

    start_server = websockets.serve(lambda ws, path: read_and_send_data(ser, ws, path), websocket_server_url, websocket_server_port)

    await start_server

    # Keep the server running until a keyboard interrupt (Ctrl+C) is received
    try:
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        # Close the serial connection when the server is shutting down
        ser.close()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
