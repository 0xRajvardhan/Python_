sub1 = int(input("Enter marks of first subject:\n"))
sub2 = int(input("Enter marks of seconds subject:\n"))
sub3 = int(input("Enter marks of third subject:\n"))

if (sub1 < 33 or sub2 < 33 or sub3 < 33):
    print("Fail")
elif (sub1 + sub2 + sub3)/3 < 40:
    print("Fail in the total percentage criteria")
else:
    print("Congratulations!")