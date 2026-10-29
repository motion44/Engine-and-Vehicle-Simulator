print("Welcome to the program! Please start by entering your vehicle information")

vehicle_make = input("Enter the make of your vehicle: ")
engine_rpm = int(input("Enter the engine RPM: "))
gear_ratio = float(input("Enter the gear ratio: "))
fd_ratio = float(input("\nEnter the final drive ratio: "))
overall_gear_ratio = gear_ratio * fd_ratio
wheel_rpm = engine_rpm / overall_gear_ratio

wheel_rpm = round(wheel_rpm, 2)

print(f"\nVEHICLE INFORMATION:")
print(f"Make: {vehicle_make}")
print(f"Engine RPM: {engine_rpm}")
print(f"Gear Ratio: {gear_ratio}")
print(f"Wheel RPM: {wheel_rpm}")
print(f"Final Drive Ratio: {fd_ratio}")
print(f"Overall Gear Ratio: {overall_gear_ratio}")
