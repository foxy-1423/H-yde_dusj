import serial
import time

# Define the COM port and baud rate
com_port = 'COM3'  # Replace 'x' with the actual COM port number
baud_rate = 9600

# Height of the sensor above the person's head (in millimeters)
sensor_height_mm = 2000  # Adjust this value as needed

# Open the COM port
ser = serial.Serial(com_port, baud_rate)

try:
    while True:
        # Read data from the COM port until 'R' is encountered
        start_char = ser.read(1).decode('utf-8')
        if start_char == 'R':
            # Read the remaining 4 characters
            data = start_char + ser.read(4).decode('utf-8')

            # Check if the data is in the expected format
            if data[1:].isdigit():
                depth_mm = int(data[1:])
                # Calculate the person's height based on the sensor's position
                height_mm = sensor_height_mm - depth_mm
                height_m = height_mm / 1000  # Convert to meters
                print(f"Height: {height_m:.2f} meters")
            else:
                print(f"Invalid data received: {data}")
        else:
            # If 'R' is not the first character, skip this message
            continue

        # Wait for 1 second (adjust as needed)
        time.sleep(1)

except KeyboardInterrupt:
    # Close the COM port when the program is interrupted (e.g., with Ctrl+C)
    ser.close()
