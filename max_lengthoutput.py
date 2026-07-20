li = input("Enter your list: ")
li = li.split()

max_length = 0
for word in li:
    if len(word)>max_length:
        max_length = len(word)
        longest_word = word
print(longest_word)
print(max_length)