myDict = {
    "fast": "In a quick manner",
    "honey": "A programer",
    "marks": [1, 2, 5],
    "anotherdict": {'honey': 'developer'},  # nested dictionarty
    1: 2
}

# this command prints all the keys of the dictionary
print(myDict.keys(), "\n", "\n")
print(list(myDict.keys()), "\n", "\n")

# this command prints values of all the keys in the dictionary
print(myDict.values(), "\n", "\n")

print(myDict.items(), "\n", "\n")

# updates the dictionary
print(myDict, "\n")
updateDict = {
    "Samay": "Friend",
    "Dhruvraj": "College Friend",
    "Divyata": "Sister"
}
myDict.update(updateDict)
print(myDict, "\n")


# IMPORTANT !!

print(myDict.get("honey1")) # This one returns 'none' (if the entered key is not present)
print(myDict["honey"]) # This one throws error if the key is not present in the dictionary

