# examines an input string for the occurrence of a letter
mystr = input('enter a string: ')
myletter = input('enter a letter to examine: ')

if myletter in mystr:
    print("Yes")
else:
    print("No")