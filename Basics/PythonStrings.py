# Strings in python are surrendered by ' ' or " "  so 'hello ' is same as "hello"

print("Hello, lilly <3")
print('Hello, lilly <3')

# hami quotes haru vitra string use garna sakchau until they surrounds with the srting

print("Hello , 'LIlly'")  # Hello, 'LIlly'

# print("He is called to "Ramesh"  ")  same same commas use garnu payene vayena feri haha


# Assign String to a Variable

a = "Hello dear Lilly"
print(a)


# Multiline String to a variable

a = "Whenever i sat to Code,I remember those days when i used to be happy with someone,it's really tragic and unpredeictable life."

print(a)


a='''i am inside three commans'''
print(a)  # Still i dont get the error and prints the outputs

# Now lets study strongs as array

# LIke aru programming launguages,python ma pani array of strings hunan like array of bytes representing the unicode bytes

a = "HellO , lILY"

print(a[3])  #this prints the index of the characterin that string in that array here prints = l

#Now lets study the looping inthe string

for x in "Bananana":
    print(x)  # B,a,n,a,n,a
    
    
#hami haru string ko length ni calculate garna sakchau by using the len() function

a = "Why the f**king is this so much cool"
print(len(a))  #output: 36

#Now Check the string

txt = "The best thing in her is her smile <3"

print("love" in txt)  #ysle k check garyo vane given string in love cha ki nai if cha vane true if chaina vane false so we got false coz usma love thena haha

#lets use if also

txt = "Why is she so Fu**Ing cute"

if "love" in txt:
    print("Yes, love is present") #THis line skips 
else:
    print("No, love is not present")  #THis line ececutes
    
    
    
    
#Let's use Check if NOT

txt = "DId she think about me as i think about her"

print("she" not in txt)  #nvako cha vane true else false




# Let's use the if NOT statement

txt = "The best thing in the world is peace and to be loved"

if "Care" not in txt:
    print("Care is not present")  #This line ececutes
    