# Chapter 20: Countdown Timer

## 🚀 Open Notebook

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/PavanMudigonda/python-bro-code/blob/main/20-timer/20-timer.ipynb) [![Open In Kaggle](https://img.shields.io/badge/Open%20in-Kaggle-20BEFF?style=flat&logo=kaggle)](https://kaggle.com/kernels/welcome?src=https://github.com/PavanMudigonda/python-bro-code/blob/main/20-timer/20-timer.ipynb)


## 📺 Video Tutorial

**Countdown timer program in Python ⌛** (8:59)

## 📺 Video Tutorial

## 📚 What You'll Learn
Build a real countdown timer using Python's time module - combining loops, time operations, and user input!

## 🎯 Learning Objectives
- Use the time module for delays
- Convert between time units (hours/minutes/seconds)
- Create countdown logic
- Format time display (HH:MM:SS)
- Build an interactive timer program
- Clear console output for better display

## 📖 Concept Explanation

### What is the Time Module?
Python's `time` module provides time-related functions like delays, current time, and time measurements.

### Key Functions
```python
import time

time.sleep(seconds)  # Pause execution
time.time()          # Current time in seconds since epoch
```

### Time Conversion
```
1 hour = 60 minutes = 3600 seconds
1 minute = 60 seconds
```

### Timer Logic
1. Get total time in seconds
2. While time > 0:
   - Display remaining time
   - Wait 1 second
   - Subtract 1 from time
3. Show completion message

## 💡 Examples

### Example 1: Basic Sleep
```python
import time

print("Starting...")
time.sleep(3)  # Wait 3 seconds
print("3 seconds have passed!")
```

### Example 2: Simple Countdown
```python
import time

for i in range(5, 0, -1):
    print(i)
    time.sleep(1)
print("Time's up!")
```

### Example 3: Seconds to Time Format
```python
def format_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"

# Examples
print(format_time(3661))  # 01:01:01
print(format_time(125))   # 00:02:05
print(format_time(7200))  # 02:00:00
```

### Example 4: Time Input Converter
```python
hours = int(input("Hours: "))
minutes = int(input("Minutes: "))
seconds = int(input("Seconds: "))

total_seconds = (hours * 3600) + (minutes * 60) + seconds
print(f"Total: {total_seconds} seconds")
```

### Example 5: Basic Countdown Timer
```python
import time

def countdown(seconds):
    while seconds > 0:
        mins = seconds // 60
        secs = seconds % 60
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")  # \r returns cursor to start
        time.sleep(1)
        seconds -= 1
    
    print("Time's up!     ")

countdown(10)
```

### Example 6: Full Featured Timer
```python
import time

print("=== Countdown Timer ===\n")

hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))

total_seconds = (hours * 3600) + (minutes * 60) + seconds

print(f"\nTimer set for: {hours:02d}:{minutes:02d}:{seconds:02d}")
print("Starting countdown...\n")

while total_seconds > 0:
    hrs = total_seconds // 3600
    mins = (total_seconds % 3600) // 60
    secs = total_seconds % 60
    
    print(f"{hrs:02d}:{mins:02d}:{secs:02d}", end="\r")
    time.sleep(1)
    total_seconds -= 1

print("🔔 Time's up!     ")
```

### Example 7: Pomodoro Timer
```python
import time

def pomodoro_session(work_mins, break_mins):
    # Work session
    print(f"Work time: {work_mins} minutes")
    countdown_minutes(work_mins)
    print("✅ Work session complete!")
    
    # Break session
    print(f"\nBreak time: {break_mins} minutes")
    countdown_minutes(break_mins)
    print("✅ Break complete!")

def countdown_minutes(minutes):
    seconds = minutes * 60
    while seconds > 0:
        mins = seconds // 60
        secs = seconds % 60
        print(f"{mins:02d}:{secs:02d}", end="\r")
        time.sleep(1)
        seconds -= 1
    print()

# 25 min work, 5 min break
pomodoro_session(25, 5)
```

### Example 8: Multiple Timers
```python
import time

def run_timer(name, seconds):
    print(f"\n{name}: {seconds} seconds")
    for i in range(seconds, 0, -1):
        print(f"{name}: {i}s remaining", end="\r")
        time.sleep(1)
    print(f"{name}: Complete!     ")

# Cooking timers
run_timer("Pasta", 10)
run_timer("Sauce", 5)
run_timer("Garlic Bread", 8)
print("\n🍝 Dinner is ready!")
```

### Example 9: Progress Bar Timer
```python
import time

def timer_with_progress(seconds):
    total = seconds
    
    for remaining in range(seconds, 0, -1):
        progress = (total - remaining) / total
        bar_length = 30
        filled = int(bar_length * progress)
        bar = "█" * filled + "░" * (bar_length - filled)
        
        mins = remaining // 60
        secs = remaining % 60
        
        print(f"[{bar}] {mins:02d}:{secs:02d}", end="\r")
        time.sleep(1)
    
    print(f"[{'█' * bar_length}] Complete! ")

timer_with_progress(15)
```

### Example 10: Interval Timer
```python
import time

def interval_timer(work_sec, rest_sec, rounds):
    for round_num in range(1, rounds + 1):
        print(f"\nRound {round_num}/{rounds}")
        
        # Work interval
        print("WORK!", end=" ")
        for i in range(work_sec, 0, -1):
            print(f"{i}...", end=" ", flush=True)
            time.sleep(1)
        
        if round_num < rounds:
            # Rest interval
            print("\nREST!", end=" ")
            for i in range(rest_sec, 0, -1):
                print(f"{i}...", end=" ", flush=True)
                time.sleep(1)
    
    print("\n\n✅ Workout complete!")

# 20 seconds work, 10 seconds rest, 3 rounds
interval_timer(20, 10, 3)
```

## 🔍 Common Mistakes

### Mistake 1: Not Importing time Module
```python
# Wrong
print("Wait 1 second...")
sleep(1)  # NameError!

# Correct
import time
print("Wait 1 second...")
time.sleep(1)
```

### Mistake 2: Wrong Time Conversion
```python
# Wrong
hours = 2
minutes = 30
total = hours + minutes  # = 2.5 (wrong!)

# Correct
total_seconds = (hours * 3600) + (minutes * 60)  # = 9000
```

### Mistake 3: Display Format Issues
```python
# Poor formatting
mins = 5
secs = 3
print(f"{mins}:{secs}")  # 5:3

# Better formatting
print(f"{mins:02d}:{secs:02d}")  # 05:03
```

### Mistake 4: Infinite Loop
```python
# Wrong - never decrements
seconds = 10
while seconds > 0:
    print(seconds)
    time.sleep(1)
    # Forgot: seconds -= 1

# Correct
seconds = 10
while seconds > 0:
    print(seconds)
    time.sleep(1)
    seconds -= 1
```

### Mistake 5: Not Clearing Previous Output
```python
# Messy output
for i in range(5, 0, -1):
    print(f"Time: {i}")
    time.sleep(1)
# Prints 5 lines

# Cleaner output
for i in range(5, 0, -1):
    print(f"Time: {i}", end="\r")
    time.sleep(1)
# Updates same line
```

## ✍️ Practice Exercises

### Easy
1. Create a 10-second countdown
2. Make a 5-minute timer
3. Convert 90 seconds to MM:SS format
4. Build a simple stopwatch
5. Create a "take a break" reminder (every 20 minutes)

### Medium
6. Build a kitchen timer with multiple alarms
7. Create a workout interval timer (30s work, 15s rest)
8. Make a Pomodoro timer (25 min work, 5 min break)
9. Build a countdown with pause/resume
10. Create a timer that accepts "5m 30s" input format

### Hard
11. Multi-timer manager (run multiple timers)
12. Timer with sound notification
13. Exam timer with warnings at intervals
14. Build a timer with progress visualization
15. Create a competitive countdown (2 players)

## 🎮 Real-World Applications

### Application 1: Study Timer
```python
import time

def study_session():
    print("=== Study Timer ===\n")
    
    study_time = int(input("Study duration (minutes): "))
    break_time = int(input("Break duration (minutes): "))
    sessions = int(input("Number of sessions: "))
    
    for session in range(1, sessions + 1):
        print(f"\n📚 Study Session {session}/{sessions}")
        countdown_min(study_time)
        
        if session < sessions:
            print(f"\n☕ Break Time!")
            countdown_min(break_time)
    
    print("\n✅ Study session complete!")

def countdown_min(minutes):
    seconds = minutes * 60
    while seconds > 0:
        m = seconds // 60
        s = seconds % 60
        print(f"{m:02d}:{s:02d}", end="\r")
        time.sleep(1)
        seconds -= 1

study_session()
```

### Application 2: Cooking Assistant
```python
import time

def cooking_timer():
    print("=== Cooking Timer Assistant ===\n")
    
    tasks = []
    
    num_tasks = int(input("How many cooking tasks? "))
    
    for i in range(num_tasks):
        name = input(f"\nTask {i+1} name: ")
        minutes = int(input(f"Minutes for {name}: "))
        tasks.append((name, minutes * 60))
    
    print("\n🍳 Starting cooking timers...\n")
    
    for name, seconds in tasks:
        print(f"\n⏰ {name} - {seconds//60} minutes")
        
        while seconds > 0:
            m = seconds // 60
            s = seconds % 60
            print(f"{name}: {m:02d}:{s:02d}", end="\r")
            time.sleep(1)
            seconds -= 1
        
        print(f"✅ {name} is ready!     ")
    
    print("\n🍽️ All cooking complete!")

cooking_timer()
```

### Application 3: Fitness Interval Timer
```python
import time

def hiit_workout():
    print("=== HIIT Workout Timer ===\n")
    
    work_time = int(input("Work interval (seconds): "))
    rest_time = int(input("Rest interval (seconds): "))
    rounds = int(input("Number of rounds: "))
    
    print("\nGet ready!")
    time.sleep(3)
    
    for round_num in range(1, rounds + 1):
        # Work phase
        print(f"\n🔥 ROUND {round_num}/{rounds} - WORK!")
        for i in range(work_time, 0, -1):
            print(f"⏱️  {i} seconds", end="\r")
            time.sleep(1)
        
        # Rest phase (except last round)
        if round_num < rounds:
            print(f"\n💚 REST")
            for i in range(rest_time, 0, -1):
                print(f"⏱️  {i} seconds", end="\r")
                time.sleep(1)
    
    print("\n\n🎉 WORKOUT COMPLETE!")

hiit_workout()
```

### Application 4: Presentation Timer
```python
import time

def presentation_timer():
    print("=== Presentation Timer ===\n")
    
    total_minutes = int(input("Presentation length (minutes): "))
    warning_minutes = int(input("Warning at (minutes remaining): "))
    
    total_seconds = total_minutes * 60
    warning_seconds = warning_minutes * 60
    
    print(f"\nTimer: {total_minutes} minutes")
    print("Starting...\n")
    
    while total_seconds > 0:
        mins = total_seconds // 60
        secs = total_seconds % 60
        
        # Warnings
        if total_seconds == warning_seconds:
            print(f"\n⚠️  {warning_minutes} minutes remaining!\n")
        elif total_seconds == 60:
            print(f"\n⚠️  1 minute remaining!\n")
        elif total_seconds == 30:
            print(f"\n⚠️  30 seconds!\n")
        
        print(f"⏱️  {mins:02d}:{secs:02d}", end="\r")
        time.sleep(1)
        total_seconds -= 1
    
    print("\n\n⏰ Time's up!          ")

presentation_timer()
```

## 🚀 Challenge Projects

### Challenge 1: Advanced Pomodoro
Create a full Pomodoro timer with:
- 25 min work / 5 min short break
- 15 min long break after 4 sessions
- Track completed sessions
- Show productivity statistics
- Save session history to file

### Challenge 2: Multi-Timer Dashboard
Build a program that:
- Runs multiple timers simultaneously
- Shows all timers in real-time
- Allows adding/removing timers
- Prioritizes by urgency
- Alerts when each timer completes

### Challenge 3: Exam Timer
Create an exam timer with:
- Total time display
- Time per question calculator
- Warnings at 50%, 25%, 10% remaining
- Pause/resume functionality
- Extra time addition

### Challenge 4: Time Tracker
Build a productivity tracker:
- Start/stop timer for tasks
- Categorize tasks (work, study, break)
- Show daily summary
- Calculate productivity percentage
- Export report

### Challenge 5: Countdown Event Timer
Create a timer for future events:
- Calculate days, hours, mins, secs until event
- Update in real-time
- Multiple event tracking
- Show percentage complete
- Milestone notifications

## 📚 Time Module Reference

```python
import time

# Pause execution
time.sleep(seconds)

# Current time (seconds since epoch)
current = time.time()

# Format time for display
time.strftime("%H:%M:%S")

# Measure elapsed time
start = time.time()
# ... code ...
elapsed = time.time() - start
```

## 🎨 Display Formatting Tricks

```python
# Overwrite same line
print("Loading...", end="\r")

# Clear to end of line
print("Done!     ", end="\r")

# Flush output immediately
print("Progress", flush=True)

# Format with leading zeros
print(f"{5:02d}")  # "05"
print(f"{12:02d}") # "12"
```

## 💪 Try It Yourself

Modify `main.py` to:
1. Add hours support
2. Show progress bar
3. Add pause/resume feature
4. Include sound notification
5. Save timer history
6. Add multiple preset timers

## 🎓 Key Takeaways from Video

1. Functions are reusable blocks of code
2. Import modules to use external code
3. Use loops to repeat actions

> 💡 *These points cover the main concepts from the video tutorial to help reinforce your learning.*

## 🔗 Next Chapter
Continue to [Chapter 20: Nested Loops](20-nested-loops.md) to learn about loops within loops!

