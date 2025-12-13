# Scope Resolution
# variable scope = where a variable is visible/accessible
# scop resolution = the order in which Python looks for a variable
# (LEGB Rule) Local -> Enclosing -> Global -> Built-in

def func1():
    x = 10  # Local scope
    print("Inside func1, x =", x)

def func2():
    x = 20  # Local scope
    print("Inside func2, x =", x)  # Will look for x in enclosing/global scope
    
func1()
func2()