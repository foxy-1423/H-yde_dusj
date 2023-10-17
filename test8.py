import serial

# Define the COM port and baud rate
com_port = 'COM3'  # Replace with your COM port name
baud_rate = 9600  # Adjust to match your sensor's baud rate

# Initialize the serial connection
ser = serial.Serial(com_port, baud_rate)

try:
    while True:
        # Read data from the COM port until a carriage return character is encountered
        data = b''
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
            except ValueError:
                print("Invalid distance data received")
except KeyboardInterrupt:
    pass

# Close the serial connection
ser.close()
