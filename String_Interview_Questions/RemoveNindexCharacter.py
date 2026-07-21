a = input("Enter your string:  ")
n = int(input("Enter the index too remove: "))
new_st = a[:n]+a[n+1:]
print(new_st)