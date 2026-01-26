# ============================================
# Chapter 19: Countdown Timer Program
# ============================================
# This program creates a countdown timer that displays
# remaining time in hours:minutes:seconds format

import time  # Import time module for sleep function

# ============================================
# Step 1: Get total time from user (in seconds)
# ============================================
my_time = int(input("Enter the time in seconds: "))

# ============================================
# Alternative: Simple countdown (commented out)
# ============================================
# time.sleep(my_time)  # Wait for specified seconds
# print("Time is up!")

# ============================================
# Step 2: Define timer function
# ============================================
def timer():
    """Countdown timer that displays remaining time"""
    
    # Loop from my_time down to 1 (step of -1 for countdown)
    for x in range(my_time, 0, -1):
        
        # ============================================
        # Time Conversion Calculations:
        # ============================================
        # Calculate hours: total seconds ÷ 3600
        hours = int(x / 3600)
        
        # Calculate minutes: (total seconds ÷ 60) mod 60
        # % 60 ensures we don't count hours as minutes
        minutes = int(x / 60) % 60
        
        # Calculate seconds: remaining seconds after hours & minutes
        # % 60 gives us the leftover seconds
        seconds = x % 60
        
        # ============================================
        # Display remaining time
        # ============================================
        print(f"{hours:02d}:{minutes:02d}:{seconds:02d} remaining")
        print(f"Total seconds left: {x}")
        
        # Wait 1 second before next iteration
        # (changed from 3 to make it a real timer)
        time.sleep(1)
    
    # ============================================
    # Timer completed
    # ============================================
    print("\n⏰ Time is up!")

# ============================================
# Step 3: Run the timer
# ============================================
timer()

# ============================================
# Time Conversion Reference:
# ============================================
# 1 hour = 3600 seconds
# 1 minute = 60 seconds
# Example: 3665 seconds =
#   Hours: 3665 ÷ 3600 = 1 hour
#   Minutes: (3665 ÷ 60) % 60 = 1 minute  
#   Seconds: 3665 % 60 = 5 seconds
#   Result: 01:01:05