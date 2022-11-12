post = input("ENTER YOUR TEXT\n")

post = post.casefold()  # casefold makes it case insesitive

if "harry" in post:
    print("Yes 'harry' is present in this post")
else:
    print("'harry' not present")
