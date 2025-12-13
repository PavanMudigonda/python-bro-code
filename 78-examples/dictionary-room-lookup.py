rooms = {1:'Foyer',2:'Conference Foyer'}
room = input("Enter your room number ?")

room = int(room)
if room not in rooms:
    print("Your room not present")
else:
    print("your room name is: "+ rooms[room])
