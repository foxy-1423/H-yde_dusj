import serial

ser = serial.Serial('COM3', 9600, timeout=1)

while True:
    # Read 5 characters from the COM port
    data = ser.read(5)
    
    # Ignore the first character
    distance = data[1:]
    
    # Extract the distance value in millimeters
    distance_mm = int(distance)
    
    print(f"Distance: {distance_mm} mm")
