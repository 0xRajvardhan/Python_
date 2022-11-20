f = open('Chapter 9\poem.txt') #this adsress  path will not work everytime

t = f.read()
if 'twinkle' in t:
    print("Twinkle is present")
else:
    print("Twinkle is not present")

f.close()