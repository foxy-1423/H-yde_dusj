import asyncio
import websockets

async def handler(websocket, path):
    num = await websocket.recv()
    print(f"Received integer: {num}")

start_server = websockets.serve(handler, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
