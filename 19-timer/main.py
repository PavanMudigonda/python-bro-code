import time

my_time = int(input("Enter the time in seconds: "))

def timer():
    for i in range(my_time, 0, -1):
        seconds = i % 60
        minutes = i // 60
        print(f"{minutes} minutes and {seconds} seconds left")
        print(i)
        time.sleep(3)
    print("Time is up!")
timer()