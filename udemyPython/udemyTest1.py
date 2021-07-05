# Variables
x = 15
price = 9.99

discount = 0.2

result = price * (1-discount)
print(result)

name = "rakin"
name = "bob"
print(name)
print(name*2)
print(name + name)

a = 25
b = a

print(a)
print(b)

a = 30
b = 17


print(a)
print(b)

#String Formatting
name = "Rakin"
greeting = f"Hello {name}"
print(greeting)

name = "Ben"
print(f"Hello {name}")

name = "john"
greeting = "wassup, {}"
with_name = greeting.format(name)
print(with_name)

name = "Kevin"
greeting = "Bye, {}" 
with_name = greeting.format(name)
with_name2 = greeting.format("Ben")
print(with_name)
print(with_name2)

longer_phrase = "Hello, {}. Today is {}."
formatted = longer_phrase.format("Patrick", "Friday")
print(formatted)

#Getting user input
name = input("Enter your name: ")
print(name)


size_input = input("How big is your house (in square feet): ")  # input function always gives back string
square_feet = int(size_input)                                   # allowing you to store an integer within variable 
square_meters = square_feet / 10.8                              # calculating square meters by using the stored variable in square feet
print(f"My house in {square_feet} square feet is about {square_meters:.2f} in square meters") 
# using f string to store the values within the string
# :.2f will format square meters into 2 decimal places







