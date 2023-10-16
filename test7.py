import serial

ser = serial.Serial('COM3', 9600, timeout=1)

while True:
    data = ser.readline().decode('ascii')
    if data.startswith('R'):
        range_in_mm = int(data[1:5])
        if range_in_mm == 5000:
            print('No target detected')
        else:
            print(f'Target detected at {range_in_mm} mm')
