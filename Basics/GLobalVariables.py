# variables  that are created outside of the function are known as the global variables

x = "22"

def myfunc():
    print("The age of my x is "+x)
    
    
myfunc()

# we can define the function as def functionname():  print("string")

x  = "awesome"

def myfunc():
    x = "goodbye"
    print("The age of my x is "+x) #here the x will take local variable
    
myfunc()

print("The age of my x is "+x)  #here the value of x will take the global variable


# lets use the global keyword

# normally tw hami variable haru function inside banauchau but that is only used inside so to create a global variable we use the global keyword

def myfunc():
    global x
    x = "Perfect"
    print("My x loos just"+x)  # yaha hamile x ko value global bata lagnu vaneko le x = awesome hune cha
    


x = "georgous"

def myfunc():
    global x
    x = "Perfect"
    print("My x is now "+x)  # yaha x = perfect hunc 

myfunc()

print("MY X is now "+x)  # yaha pani x = perfect