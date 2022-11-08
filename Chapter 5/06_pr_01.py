myDict = {
    "Pankha": "Fan",
    "Dabba": "Box",
    "Vastu": "Item"
}
print("Options are ", myDict.keys())

a = input("Enter a Hindi word:\n")
# print("The meaning of your word is:", myDict[a])

print("The meaning of your word is:", myDict.get(a))