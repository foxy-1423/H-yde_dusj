import serial
import asyncio
import websockets

# Define the COM port and baud rate
com_port = 'COM3'  # Replace with your COM port name
baud_rate = 9600  # Adjust to match your sensor's baud rate

# Define the WebSocket server URL
websocket_server_url = "ws://localhost:8765"  # Replace with the WebSocket server URL

async def read_and_send_data(ser, websocket):
    try:
        while True:
            # Read 10 bytes from the COM port
            data = await asyncio.get_event_loop().run_in_executor(None, ser.read, 10)

            # Process the data if it's not empty
            if data:
                # Extract the last 4 characters as the distance value
                distance_str = data[-4:].decode('utf-8')

                # Convert the distance value to an integer
                try:
                    distance = int(distance_str)
                    print(f"Distance: {distance} units")

                    # Send the distance data to the WebSocket server
                    await websocket.send(distance_str)
                except ValueError:
                    print("Invalid distance data received")
    except KeyboardInterrupt:
        pass


async def main():
    # Initialize the serial connection
    ser = serial.Serial(com_port, baud_rate)
    
    async with websockets.connect(websocket_server_url) as websocket:
        await read_and_send_data(ser, websocket)

    # Close the serial connection
    ser.close()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
