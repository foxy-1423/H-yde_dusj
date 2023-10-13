import serial
import asyncio
import websockets

async def send_data_to_websocket():
    async with websockets.connect('ws://localhost:8765') as websocket:
        ser = serial.Serial('COM3', 9600, timeout=1)
        while True:
            data = ser.readline().decode('utf-8').strip()
            if len(data) == 5 and data[0] != ' ':
                try:
                    value = int(data[1:])
                    print(value)
                    await websocket.send(str(value))
                except ValueError:
                    pass

asyncio.get_event_loop().run_until_complete(send_data_to_websocket())
