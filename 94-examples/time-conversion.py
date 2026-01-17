def greeting(seconds):
    hours = seconds //3600   # 1 hour
    minutes = (seconds - hours *3600 ) // 60  # 300/60 = 5 mins
    remaining_seconds = seconds - ( (hours * 3600) + (minutes * 60) )   # 0 seconds
    return hours, minutes, remaining_seconds

hours, minutes, remaining_seconds = greeting(3900)

print(hours, minutes, remaining_seconds)
