with open('Chapter 9/IBM log.txt') as f:
    content = f.read()

if 'python' in content.lower(): #this lower command helps to prevent issues that get raised due to case sensitivity
    print("Yes python is present")