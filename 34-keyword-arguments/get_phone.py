# default arguments = A default value for certain parameters
#                     default is used when that argument is omitted
#                     make your functions more flexible, reduce # of arguments
#                     1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary


def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

# phone_num = get_phone(1,547,000,0000)

phone_num = get_phone(country="+1",area="547",first="000",last="0000")

print(phone_num)