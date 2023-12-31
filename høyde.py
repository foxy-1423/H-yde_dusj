import serial
import time

# Define the COM port and baud rate
com_port = 'COM3'  # Replace 'x' with the actual COM port number
baud_rate = 9600

# Initialize sensor_height_mm to a default value
sensor_height_mm = 2000  # Default height in millimeters

# Open the COM port
ser = serial.Serial(com_port, baud_rate)

# Perform calibration on startup
print("Performing calibration. Please ensure there is no one under the sensor.")
time.sleep(5)  # Allow some time for any residual data to be cleared

calibration_samples = []
for _ in range(10):
    raw_data = ser.read(4).decode('utf-8')
    if raw_data.startswith('R') and raw_data[1:].isdigit():
        depth_sample_raw = int(raw_data[1:])
        calibration_samples.append(depth_sample_raw)
        print(f"Raw Sensor Value: {depth_sample_raw} mm")
    else:
        print(f"Invalid data received during calibration: {raw_data}")
    time.sleep(0.5)

# Calculate the sensor height based on the maximum depth reading
if calibration_samples:
    sensor_height_mm = max(calibration_samples)
    print(f"Calibration complete. Sensor height set to {sensor_height_mm} mm.")
else:
    print("Calibration failed. Unable to determine sensor height.")

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

