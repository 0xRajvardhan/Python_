for i in range(10):
    print(i)
    if i == 5:
        break
else:
    print("This is inside else of for")

    # this else statement will not work because of break statement fired
