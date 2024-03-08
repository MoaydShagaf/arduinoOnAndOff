from pymata4 import pymata4
import time

# Configuration
command_file = "command.txt"
led_pin = 11  # Adjust to your LED pin
board = pymata4.Pymata4(com_port='COM65', baud_rate=57600)

# Initialize LED pin
board.set_pin_mode_digital_output(led_pin)
# Ensure the LED is off initially
board.digital_write(led_pin, 0)

def read_command():
    try:
        with open(command_file, "r") as file:
            command = file.readline().strip()
        # Clear the file after reading
        with open(command_file, "w") as file:
            file.write("")
        return command
    except FileNotFoundError:
        return ""

def execute_command(command):
    if command == "ON":
        board.digital_write(led_pin, 1)
        print("LED Turned ON")
    elif command == "OFF":
        board.digital_write(led_pin, 0)
        print("LED Turned OFF")

if __name__ == "__main__":
    while True:
        command = read_command()
        if command:
            execute_command(command)
        time.sleep(0.5)  # Check for new commands every half second
