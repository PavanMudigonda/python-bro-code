x={}
print(type(x))

file_counts = {'txt':10,'pdf':11,'csv':12,'jpg':13,'py':14}



print(file_counts)


print(file_counts['txt'])

print('jpg' in file_counts)

print("-----------")

print(file_counts.items())

print(file_counts.keys())

print(file_counts.values())

for item in file_counts.items():
    print(item)

for key in file_counts.keys():
    print(key)

for value in file_counts.values():
    print(value)


print("-----------")

file_counts['pdf'] = 15

print(file_counts)

del file_counts['txt']

print(file_counts)


for extension in file_counts:
    print(extension)


for ext, amount in file_counts.items():
    print("There are {} files with extension '{}'".format(amount, ext))

print("----------")


