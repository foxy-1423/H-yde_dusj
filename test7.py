import serial

ser = serial.Serial('COM3', 9600)  # Replace 'COMx' with your actual serial port name

while True:
    line = ser.readline().decode('utf-8').strip()
    print(f"Received: {line}")
    
    if line.startswith('R') and len(line) == 6:
        try:
            range_mm = int(line[1:5])
            if range_mm == 5000:
                print("No target detected")
            else:
                print(f"Range: {range_mm} mm")
        except ValueError:
            print("Invalid data format")
    else:
        print("Invalid data format")

ser.close()
