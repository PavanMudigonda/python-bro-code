
# *args  = allows you to pass multiple non-keyword arguments
# **kwargs = allows you to pass multiple keyword arguments
# * and ** are unpacking operators
# Argument types:
# 1. positional
# 2. default
# 3. keyword
# 4. arbitrary


def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg, end=" ")
    print("\n")
    # for key,value in kwargs.items():
    #     print(f'{key} : {value}')
    if "apt" in kwargs:
        print(f'{kwargs.get('apt')} - {kwargs.get('street_number')} {kwargs.get('street_name')}')
    else:
        print(f'{kwargs.get('street_number')} {kwargs.get('street_name')}')        
    print(f'{kwargs.get('city')} , {kwargs.get('state')} , {kwargs.get('postal_code')}')
shipping_label("Dr", "Spongebob", "Squarepants", "III",
               street_number="123",
               street_name="Front St",           
               apt="1301",
               city="Toronto",
               state="ON",
               postal_code="M5V3A4")