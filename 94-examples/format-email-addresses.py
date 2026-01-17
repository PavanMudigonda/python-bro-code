def full_emails(people):
    result=[]
    for email,name in people:
        result.append("{} <{}>".format(name, email))
    return result

print(full_emails([("mvchandu.m@gmail.com","Chandu Mudigonda" ),("Naga Pavan Mudigonda","mnpawan@gmail.com")]))



