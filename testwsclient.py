import asyncio
import websockets

async def test_client():
    uri = "ws://localhost:8765"  # Replace with your WebSocket server URI
    async with websockets.connect(uri) as websocket:
        # Wait for and print any messages received from the server
        async for message in websocket:
            print(f"< Received: {message}")

# Run the client
asyncio.get_event_loop().run_until_complete(test_client())
