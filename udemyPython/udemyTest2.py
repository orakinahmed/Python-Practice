# Lists, tuples, and sets 
# Lists are the most standard collection used to add and remove elements, as well as modification

l = ["Bren", "Randy", "Jojo"]   # Lists CAN be changed by adding or removing elements

t = ("Bren", "Randy", "Jojo")   # Tuples CAN'T be modified by adding or removing elements

s = {"Bren", "Randy", "Jojo"}   # Sets CAN be changed by adding or removing elements but CAN'T have duplicate elements

# Lists and tuples keep the order of the elements
# Sets don't keep to the order, the order isn't guaranteed so the order can change at any moment

#Subscript Notation:
print(l[0]) # allowed

print(t[1]) # allowed

# sets don't allow subscript notation

# Modifying individuals items in a list:
l[0] = "Trent"
print(l)

# Add items to a list:
l.append("Leonard")     # l is the name of the list, fullstop means "inside", append means "add"
l.append("Leonard")     # Can add duplicate items within a list
print(l)


# Remove items from a list:
l.remove("Randy")
print(l)

# Adding items to a set:
s.add("Stacy")
s.add("Stacy")          # Can only add once as there can be no duplicate items within a set
print(s)

# Advanced set operations-----------------------------------------------------------------------------------------------------------------------------------
# Subtraction

friends = {"Ben", "Ren", "Jen"}   
abroad = {"Ben", "Jen"}

local_friends = friends.difference(abroad)             # Calls the difference function inside friends, and removes the elements within "abroad"
print(local_friends)                                   # Prints Ren because Ben and Jen are removed from the abroad set

local_friends = abroad.difference(friends)             # Calls the difference function inside abroad, and removes the elements within "friends"
print(local_friends)                                   # Prints an empty set because Ben and Jen are removed from friends set, and Ren doesn't exist inside friends set

# Addition
close = {"Rat"}
distant = {"Cat", "Dog"}

pets = close.union(distant)
print(pets)

# Finding both/similar elements
upper = {"Kevin", "Shajid", "Rakin", "Brian"}
lower = {"Kevin", "Shajid", "Faraz", "Ali"}

both = upper.intersection(lower)
print(both)

similar = lower.intersection(upper)     # gives same output as above^
print(similar)