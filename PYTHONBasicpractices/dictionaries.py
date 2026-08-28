dict = {1:'I',2:'am',3:'sid'}
print(dict)

#Adding elements in dictionary
Dict = {}
print("Empty dictionary")
print(Dict)

Dict[0] = 'Sid'
Dict[1] = 'is'
Dict[2] = 'great'

print("dictionary after adding elements")
print(Dict)

#Accessing element in a dictionary
print(Dict[1])

#get() method - it is used to access dictionary safely
print(Dict.get(2))

#Accessing element of a nested Dictionary
Dictionary = {'Dict1':{1:'Vartika'},
        'Dict2':{2:'Siddharth'}}

print(Dictionary['Dict1'])
print(Dictionary['Dict2'][2])

#Deleting element using del keyword
Dic = {'name':'Siddharth',1:'Saxena',3:'Guna'}
print(Dic)

del(Dic[1]) #del keyword
print(Dic)
