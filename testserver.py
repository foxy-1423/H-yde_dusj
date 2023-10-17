import asyncio
import websockets

async def receive_data(websocket, path):
    try:
        async for message in websocket:
            print(f"Received data from client: {message}")
    except websockets.exceptions.ConnectionClosedError:
        print("Connection closed.")

if __name__ == "__main__":
    start_server = websockets.serve(receive_data, "0.0.0.0", 8765)  # Replace with the desired host and port

    asyncio.get_event_loop().run_until_complete(start_server)
    print("WebSocket server is running.")
    asyncio.get_event_loop().run_forever()
