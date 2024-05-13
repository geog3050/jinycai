mylist = [2, 8, 64, 16, 32, 4, 16, 8] # example list
has_duplicate = False
for i in mylist:
    valueCount = mylist.count(i)
    if valueCount > 1:
        has_duplicate = True
        print("The list contains duplicate values")
        break
    
if not has_duplicate:
    print("The list does not contain any duplicate values")
