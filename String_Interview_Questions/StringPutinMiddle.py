a =input("enter the string")
b = input("enter the string you want in put in middle")
c =a[:len(a)//2] + b + a[len(a)//2:]
print(c)