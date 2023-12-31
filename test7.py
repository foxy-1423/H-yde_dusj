import serial

# Define the COM port and baud rate
com_port = 'COM1'  # Replace with your COM port name
baud_rate = 9600  # Adjust to match your sensor's baud rate

# Initialize the serial connection
ser = serial.Serial(com_port, baud_rate)

try:
    while True:
        # Read a line of data from the COM port
        data = ser.readline()
        
        # Process the data if it's not empty
        if data:
            # Assuming your data format is "X1234\n", extract the last 4 characters
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
