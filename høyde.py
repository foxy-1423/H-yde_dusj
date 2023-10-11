import serial  # For COM port communication
import time

# Function to configure the COM port
def configure_com_port():
    com_port = input("Enter the COM port name (e.g., COM1): ")
    baud_rate = int(input("Enter the baud rate: "))

    try:
        ser = serial.Serial(com_port, baud_rate)
        return ser
    except serial.SerialException as e:
        print(f"Error opening the COM port: {e}")
        return None

# Function to read data from the depth sensor
def read_sensor_data(ser):
    try:
        data = ser.readline().decode().strip()
        data = data[1:]  # Remove the first character regardless of what it is
        distance_mm = float(data) if data.isdigit() else None
        return distance_mm
    except Exception as e:
        print(f"Error reading data from the sensor: {str(e)}")
        return None

# Function to automatically calibrate the sensor when no one is present
def auto_calibrate_sensor(ser):
    print("Please ensure no one is standing under the sensor.")
    time.sleep(5)  # Wait for a few seconds to ensure no one is under the sensor

    # Read the sensor data multiple times and calculate the average
    readings = []
    for _ in range(10):
        distance_mm = read_sensor_data(ser)
        if distance_mm is not None:
            readings.append(distance_mm)
            print(f"Calibration Reading {len(readings)}: {distance_mm} mm")

    if readings:
        average_distance = sum(readings) / len(readings)
        print(f"Calibration Complete. Average Height: {average_distance} mm")
        return average_distance  # Return the calibration value

    return None

# Main program
if __name__ == "__main__":
    # Configure the COM port
    ser = configure_com_port()
    sensor_height = None  # Initialize the sensor height

    while True:
        # Continuously run calibration and height calculation
        calibration_value = auto_calibrate_sensor(ser)
        if calibration_value is not None:
            sensor_height = calibration_value  # Update the sensor height

        while True:
            # Read data from the depth sensor
            distance_mm = read_sensor_data(ser)

            if distance_mm is not None and sensor_height is not None:
                # Calculate the person's height based on sensor data and calibration
                person_height = sensor_height - distance_mm

                print(f"Person's height: {person_height} mm")

    # Close the COM port when done
    ser.close()
