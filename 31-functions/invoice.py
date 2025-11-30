def display_invoice(username, amount, due_date):
    print(f"Hello, {username}")
    print(f"Your bill amount of ${amount:.2f} is due: {due_date}")
    

display_invoice("JohnDoe", 100.09, "01/02")