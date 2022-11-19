this = "    honey is good    "
print(this)
print(this.strip())  # removes anything mentioned in paranthesis


def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr


test = "  haku-na-matata honey"
word = input("Enter a word to remove: ")
print(remove_and_split(test, word))
