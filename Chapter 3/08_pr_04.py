st = "This is a string with double  spaces"

doubleSpaces = st.find("  ")
print(doubleSpaces)

st = st.replace("  ", " ")
print(st)