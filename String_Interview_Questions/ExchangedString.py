st = input("Enter a string: ")
a = st[0]
b = st[-1]
st = b + st[1:-1] + a
print(st)