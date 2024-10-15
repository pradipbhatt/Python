# Python - Output Variables

# hamilae tha vayeko print() function also used to output variables

x = "Too good that's why she left"
print(x)

# now add the many variables and values

x = "Python"
y= "JS"
z = 11.11

print(x,y,z) #here we print the many varaibles at once

# we can also use the format() function to print variables

x = "Python"
y= "JS"
z = 11.11

print(f"I love {x} and {y}, the average of {z} is {z/2}") #here we print the many varaibles at once using format() function
# Tya agadi use vayeko f stants for format function

# Lets use the + operator to assign the multiple variables

x = "Python"
y= "JS"
z = "dear lily"

print(x+y+z) # but here is hack we cant concatenate srings with the numbers and floats we just concatenate strings with strings 
# because + operator only works for strings

x=3
y=5
print(x+y) # here + operator is used for summation of these numbers

# we can convert the numbers to strings using str() function

x=3
y=5
print(str(x)+str(y)) #numbers lae concatenate garna ko lage we use str() function



# Python - Strings
# we can also use the * operator to repeat the strings
x="Python "
print(x*3) # here * operator is used for repetition of the string output = python python python


# best way to output the multiple variables is using the comma operator

x=5
y = "John shelby" #string takes white speaces as well
print(x,y)