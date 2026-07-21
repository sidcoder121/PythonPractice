# write a python program to remove the given string of odd values

st = input("Enter your String: ")
new_st  = ""
for i in range(len(st)):
    if i%2==0:
        new_st+= st[i]
print(new_st)