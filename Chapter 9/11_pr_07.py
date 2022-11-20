content = True
i = 1
with open('Chapter 9/IBM log.txt') as f:
    
    while content:
        content = f.readline()

        if 'python' in content.lower():  # this lower command helps to prevent issues that get raised due to case sensitivity
            print(content)
            print("Yes python is present")
            print(i)
        i += 1
