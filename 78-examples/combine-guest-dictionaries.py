def combine_guests(guests1, guests2):
    # Combine both dictionaries into one, with each key listed
    # only once, and the value from guests1 taking precedence
    guests3 = guests1 | guests2
    return guests3


Rorys_guests = {"Adam": 2, "Brenda": 3, "David": 1, "Jose": 3, "Charlotte": 2, "Terry": 1, "Robert": 4}
Taylors_guests = {"David": 4, "Nancy": 1, "Robert": 2, "Adam": 1, "Samantha": 3, "Chris": 5}

print(combine_guests(Rorys_guests, Taylors_guests))


def combine_guests_alternative(guests1, guests2):
    # Alternative method using copy and update
    guests3 = guests1.copy()
    guests3.update(guests2)
    return guests3


print(combine_guests_alternative(Rorys_guests, Taylors_guests))
