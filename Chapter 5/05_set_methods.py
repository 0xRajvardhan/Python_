# Creating a set
b = set()
print(type(b))

# Adding
b.add(3)
b.add(4)
b.add(5)
b.add(6)
print(b)
# cannot add list in set because list is unhashable
# we can also not add dictionaries for the same reason
# but we can add tuple
b.add((4, 5, 6))
print(b)

print(len(b))# prints number of items in "b"

b.remove(3) # removes the entered element
print(b)

print(b.pop()) # removes an element randomly and "returns" it
print(b)

print(b.clear()) # empties the set

print(b.union())
print(b.intersection())
