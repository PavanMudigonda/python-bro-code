def replace_domain(email,old_domain,new_domain):
    if "@" + old_domain in email:
        index = email.index("@"+old_domain)
        new_email=email[:index]+"@"+new_domain
        return new_email
    return email




replace_domain("mnpawan@yahoo.com","mnpawan@ymail.com", "mnpawan@gmail.com")


