def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = ( seconds - hours *3600 ) // 60
    remaining_seconds = seconds - ( hours * 3600) - ( minutes * 60 )
    return hours,minutes,remaining_seconds

result = convert_seconds(5000)
print(result)
print(type(result))



result = convert_seconds(6000)
print(result)
