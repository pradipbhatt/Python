# Builtin data types are
# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

x = 18

print(type(x))

x = "Hello, am watching at you right now"

print(type(x))

x = 11.11

print(type(x))

x = [1,2,3,4,5]

print(type(x))

x = (1,2,3,4,5)

print(type(x))

x = range(1,6)

print(type(x))

x = {
    "name": "John", 
    "age": 30}

print(type(x))

x = {"apple", "banana", "cherry"}

print(type(x))

x = True

print(type(x))

x = b"Hello, am watching at you right now"

print(type(x)) #bytes datatypes

x = bytearray(5) # bytearray datatypes

print(type(x))

# setting the specific datatype

x = str(23)  # number is changed to string typecasting here

print(type(x))

x = int(11.11)  # float is changed to integer typecasting here

print(type(x))


# <class 'int'>
# <class 'str'>
# <class 'float'>
# <class 'list'>
# <class 'tuple'>
# <class 'range'>
# <class 'dict'>
# <class 'set'>
# <class 'bool'>
# <class 'bytes'>
# <class 'bytearray'>
# <class 'str'>
# <class 'int'>