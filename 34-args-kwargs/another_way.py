
def show_kwargs_details(**kwargs):
    # Show all keys
    print("Keys:")
    for key in kwargs.keys():
        print(f"  {key}")

    # Show all values
    print("\nValues:")
    for value in kwargs.values():
        print(f"  {value}")

    # Show key-value pairs
    print("\nKey-Value Pairs:")
    for key, value in kwargs.items():
        print(f"  {key} -> {value}")


# Call the function
show_kwargs_details(name="Alice", age=30, city="Toronto", country="Canada")
