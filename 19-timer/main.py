import time

my_time = int(input("Enter the time in seconds: "))

# time.sleep(my_time)
# print("time is up")

def timer():
    for x in range(my_time, 0, -1): # countdown in reverse way
        hours = int(x / 3600) # first find the remaining hours
        minutes = int(x / 60) % 60  # second find the remaining minutes
        seconds = x % 60 # finally find the remaining seconds
        print(f"{hours} hours, {minutes} minutes and {seconds} seconds left")
        print(x)
        time.sleep(3)
    print("Time is up!")
timer()