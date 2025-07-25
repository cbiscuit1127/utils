import time
import subprocess
import datetime as dt

cls = lambda: subprocess.run(['cls'], shell=True)

def clock():
    """Return the current time in HH:MM:SS format."""
    while True:
        cls()
        print(dt.datetime.now().strftime("%H:%M:%S"))
        time.sleep(1)

def timer(count: int = 30):
    """Run a timer that prints the current time every second."""
    for i in range(3, 0, -1):
        cls()
        print(f'Starting in {i} seconds...')
        time.sleep(1)
    else:
        cls()
        print('Go!')
        time.sleep

    for i in range(count, 0, -1):
        cls()
        print(f'Time left: {i} s.')
        time.sleep(1)
    else:
        cls()
        print('Game over!')
        time.sleep(1)

def alarm(h: int, m: int):
    """Set an alarm for a specific hour and minute."""
    now = dt.datetime.now()
    while now.hour != h or now.minute != m:
        cls()
        print(f'Current time: {now.strftime("%H:%M:%S")}. Waiting for alarm at {h:02}:{m:02}...')
        time.sleep(1)
        now = dt.datetime.now()
    print(f'Alarm! The time is now {now.strftime("%H:%M:%S")}.')
    time.sleep(1)
        # if now.hour == h and now.minute == m:
        #     print(f'Alarm! The time is now {now.strftime("%H:%M:%S")}.')
        #     time.sleep(10)  # Wait for 10 seconds before checking again
        # else:
        #     print(f'Current time: {now.strftime("%H:%M:%S")}')
        #     time.sleep(1)

if __name__ == '__main__':
    print("Choose an option:")
    print("1. Clock")
    print("2. Timer")
    print("3. Alarm")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        clock()
    elif choice == '2':
        timer()
    elif choice == '3':
        h = int(input("Enter hour (0-23): "))
        m = int(input("Enter minute (0-59): "))
        alarm(h, m)
    else:
        print("Invalid choice. Exiting.")