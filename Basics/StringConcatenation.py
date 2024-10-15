#COncatenate means 1+1=11 haha my own logic

a= "Hello"
b=" Lilly"
c=a+ "" +b

print(c)


#Format-Strings

# Lets talk about the F-strings it's introduced in 3.6 to specify the string as f-string we simply put the f in the front of the string of the literal and add curly brackets f{} to the end of the string

a= "Hello"
b=" Lilly"
c=f"{a} {b}"

print(c)


#PLaceholders and MOdifieds

price = 150
txt = f"The price of the book is {price}"
print(txt)

# A modifier is included by adding a colon : followed by a legal formatting type like .2f which means fixed point nuber with 2 decimals

price = 111

txt = f"THe price of the copy is {price:.2f}" 

print(txt)  #o/p is the price of the copy is 111.00
