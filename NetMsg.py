import os
import platform

os_info = platform.system()
os_version = platform.version()

def windows(ip, message):
    os.system(f"msg * /server:{ip} {message}")

def linux(message):
    os.system(f"notify-send '{message}'")

def mac(message):
    os.system(f"osascript -e 'display notification \"{message}\" with title \"Message\"'")

if os_info == "Windows":
    if "Pro" in os_version:
        can_send_message = True
    elif "Home" in os_version:
        can_send_message = False
    else:
        can_send_message = False

elif os_info == "Linux":
    can_send_message = True

elif os_info == "Darwin":
    can_send_message = True

else:
    can_send_message = False

if can_send_message:
    ip = str(input("Enter the target's IP (or leave blank for local message): "))
    message = str(input("Enter the message you want to send: "))
    loop = input("Do you want a normal loop or infinite loop? (normal/infinite): ")

    if loop == "normal":
        times = int(input("Enter how many times you want to send the message: "))
        for i in range(times):
            if os_info == "Windows":
                windows(ip, message)
            elif os_info == "Linux":
                linux(message)
            elif os_info == "Darwin":
                mac(message)

    elif loop == "infinite":
        while True:
            if os_info == "Windows":
                windows(ip, message)
            elif os_info == "Linux":
                linux(message)
            elif os_info == "Darwin":
                mac(message)

    else:
        print("Invalid input. Please enter 'normal' or 'infinite'")
else:
    print("Your OS does not meet the requirements for sending messages.")