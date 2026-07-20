st = input("Enter the String: ")
for char in st:
    if char == st[0]:
        st = st.replace(char,"$")
print(st)