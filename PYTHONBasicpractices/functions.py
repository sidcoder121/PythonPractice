'''def function_name(parameters):
    #satement
    return expression'''
    
#creating a function
def func():
    print('Welcome in function')

func() #call a function

#create a function to add numbers
def add(num1:int,num2:int):
    num3 = num1 + num2
    return num3

print(add(6,4))

#default arguments
def myfunc(x,y=10):
    print("x : ",x)
    print("y : ",y)

myfunc(20)

def subtract(num1:int,num2:int):
    print(num1-num2)

subtract(10,8)

def mult(num1:int,num2:int):
    print(num1*num2)

mult(7,5)