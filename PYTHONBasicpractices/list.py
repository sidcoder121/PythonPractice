#create a list 
data = ["Apple","Orange","Grapes"]
print(data)

# create a list with distinct(duplicate elements)
list1 = [1,2,'sid']
print(list1)

#accessing elements from list
print(data[0])
print(data[1])

#Take input of python list
string = input('Enter your list: ')
list = string.split()
print("The list is :",list)


#adding element in a list
list2 = [1,2,3]
print(list2)

list2.append(4)
list2.append(5)
list2.append(6)

print('list after append: ', list2)

# list.insert(position,value)
list2.insert(3,12)
print(list2)

#list.extend()-  used to push multiple item in a list
list2.extend([11,'siddharth',"saxena"])

#Remove elements in the list
list2.remove(5)
print(list2)

#pop(index) - pop() remove item at last index or pop(index) at given index
list2.pop()
print(list2)