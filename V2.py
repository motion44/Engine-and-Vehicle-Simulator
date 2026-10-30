gear_ratios = {
    1: 3.50,
    2: 2.10,
    3: 1.40,
    4: 1.00,
    5: 0.80,
    6: 0.65
}

#Functions
def calculate_overall_ratio(gear_ratio, fd_ratio):
    return gear_ratio * fd_ratio  

def calculate_wheel_rpm(engine_rpm, overall_gear_ratio):
    return engine_rpm / overall_gear_ratio

def calculate_speed_kmh(wheel_rpm, tire_circumference):
    return (wheel_rpm * tire_circumference * 60 / 1000)


print("Welcome to the program! Please start by entering your vehicle information")

vehicle_make = input("Enter the make of your vehicle: ")
engine_rpm = int(input("Enter the engine RPM: "))

while True:

        gear = int(input("Enter the gear you are currently using: "))
        if gear not in gear_ratios:
            print("Invalid gear entered. Please enter a gear between 1 and 6.")            
        else:
            break

fd_ratio = float(input("\nEnter the final drive ratio: "))
tire_circumference = float(input("Enter the tire circumference: "))


gear_ratio = gear_ratios.get(gear)
overall_gear_ratio = calculate_overall_ratio(gear_ratio, fd_ratio)
wheel_rpm = calculate_wheel_rpm(engine_rpm, overall_gear_ratio)
speed_kmh = calculate_speed_kmh(wheel_rpm, tire_circumference)

wheel_rpm = round(wheel_rpm, 2)
speed_kmh = round(speed_kmh, 2)

print(f"\nVEHICLE INFORMATION:")
print(f"Make: {vehicle_make}")
print(f"Engine RPM: {engine_rpm}")
print(f"Gear Ratio: {gear_ratio}")
print(f"Wheel RPM: {wheel_rpm}")
print(f"Final Drive Ratio: {fd_ratio}")
print(f"Overall Gear Ratio: {overall_gear_ratio}")
print(f"Vehicle Speed: {speed_kmh} km/h")
