import subprocess
from tqdm import tqdm
import time

class colors:
    RESET = "\033[0m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"

def quitcode():
    time.sleep(1)
    print(colors.RED + 'Now quitting.' + colors.RESET)
    time.sleep(2)
    exit()
def userinput(check):
    if check.lower() == "h":
        print('Commands_______________ ')
        print('v for version')
        print('-------------')
        print('h for help')
        print('-------------')
        print('enter to begin scanning')
        print('-------------')
        print('Happy sniffing! ett1cal')
        print('-------------------------')
        quitcode()
    elif check.lower() == "enter":
        return
    elif check.lower() == "v":  # Removed extra colon
        print('This is TerminalScan v1.0')
        time.sleep(1)
        print('Now quitting.')
        time.sleep(2)
        exit()
def run_command():
    for _ in tqdm(range(10), desc="Searching for networks"):
        time.sleep(0.1)  # Simulate some work being done

print('Welcome to terminal scan')

check = input('press h to view help or type enter to run: ')
userinput(check)

if check.lower() == "enter":
    run_command()


def get_visible_networks_windows():
    result = subprocess.run(["netsh", "wlan", "show", "network"], capture_output=True, text=True)
    print(colors.GREEN + result.stdout + colors.RESET)

get_visible_networks_windows()
