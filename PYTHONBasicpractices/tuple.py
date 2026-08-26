Tuple1 = tuple('Sid')
print(Tuple1)

#Accesing tuple with indexing
print(Tuple1[0])

#Tuple unpacking
Tuple2 = ("I","am","Ironman")
a,b,c = Tuple2
print("value after unpacking \n")
print(a)
print(b)
print(c)

#concatenation of tuple
Tuple3 = Tuple1 + Tuple2
print(Tuple3)

#Slicing of tuple
Tuple4 = tuple('Siddhrth')
print(Tuple4[1:])

#Reversing the list
print("Reversed Tuple \n", Tuple1[: :-1])