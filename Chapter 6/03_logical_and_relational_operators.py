age = int(input("Enter your age:\n"))

if age > 34 and age < 56:  # both conditions should be true
    print("You can work with us")
else:
    print("You cannot work with us")

# Now
college = "none"
skill = "high"

if college == "reputed" or skill == 'high':  # any one condition should be true
    print("You are selected")
else:
    print("You are rejected")

# Not operator
farmaish_prui = True

if not farmaish_prui:
    print("Nakhre chalu")
else:
    print("No nakhre")
