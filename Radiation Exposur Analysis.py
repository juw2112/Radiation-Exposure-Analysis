# This is a program that will handle radiation exposure by taking 
# numberous measurements and calculates certain statistical results.

# Function to calculate average radiation level.
def calculate_average(data):
    total = sum(data)
    average = total / len(data)
    return average

# Function to calculate standard deviation.
def calculate_std_dev(data, average):
    variance = sum((x - average) ** 2 for x in data) / len(data)
    std_dev = variance ** 0.5
    return std_dev

# Initialise variables.
locations_data = []     # List to store data for each location.
continue_input = True   # Variable to control the input loop.

# Main loop for data input.
while continue_input:
    location_name = input("Enter location name (or type 'done' to finish): ")
    
    # Check if user wants to finish inputting data.
    if location_name.lower() == "done":
        break
    
    measurements = []   # List to store radiation measurements for the current location.

    # Loop to input measurements for the current location.
    while True:
        try:
            # Input a radiation measurement.
            measurement = input("Enter radiation measurement (or type 'done' to finish): ")
            if measurement.lower() == "done":
                break
            measurement = float(measurement)
            if measurement < 0:
                raise ValueError("Measurement must be a non-negative.")
            measurements.append(measurement)    # Add the measurement to the list.
        except ValueError as e:
            print("Invalid input. Please enter a valid non-negative number.")
            continue        # Continue to the next interation if the input is invalid.
    
    # Add the location name and measurements to the locations_data list.
    locations_data.append({"location": location_name, "measurements": measurements})

# Print locations along with their measurements.
print("\nLocations with their measurements:")
for location_data in locations_data:
    location = location_data["location"]
    measurements = location_data["measurements"]
    print(f"{location}: {measurements}")

# Process data and calculate statistics.
for location_data in locations_data:
    location = location_data["location"]
    measurements = location_data["measurements"]
    
    # Calculate average radiation level and standard deviation.
    try:
        avg_radiation = calculate_average(measurements)
        std_dev = calculate_std_dev(measurements, avg_radiation)
    except ZeroDivisionError:
        print(f"No measurements recorded for {location}.  Skipping calculations.")
        continue
    
    # Print statistics for the current location.
    print(f"\nLocation: {location}")
    print(f"Average Radiation Level: {avg_radiation:.2f}")
    print(f"Standard Deviation: {std_dev:.2f}")

print("\nData processing completed.")
