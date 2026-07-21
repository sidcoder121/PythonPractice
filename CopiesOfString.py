a = input("Enter a string: ")
if len(a)>2:
    b  = a[-2: ]*4
    print(b)
else:
    print("The length of string is too small")