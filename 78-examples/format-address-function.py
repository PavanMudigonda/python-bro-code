def format_address(address_string):
    # Declare variables
    house_number = ""
    street_name = []

    # Separate the address string into parts
    parts = address_string.split()

    # Traverse through the address parts
    for part in parts:
        # Determine if the address part is the
        # house number or part of the street name
        if part.isdigit():
            house_number = part
        else:
            street_name.append(part)

    # Join street name parts
    street = " ".join(street_name)

    # Return the formatted string
    return "house number {} on street named {}".format(house_number, street)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"
