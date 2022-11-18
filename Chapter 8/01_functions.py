marks1 = [45, 78, 86, 77]
percentage1 = sum(marks1)/len(marks1)
print(percentage1, "%")

# function for the same


def percentage(marks):
    return (sum(marks)/len(marks))


# now lets use this
marks2 = [75.98, 86, 77]
percentage2 = percentage(marks2)
print(percentage2)