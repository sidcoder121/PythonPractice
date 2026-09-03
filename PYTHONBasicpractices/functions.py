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

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(4)) 

def greet(greeting):
    print(greeting)

greet("Hello, welcome to the function tutorial!")

def divide(num1:int,num2:int):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    else:
        return num1 / num2

print(divide(10, 2))
print(divide(10, 0))

def PrintFun():
    print("I am function")
PrintFun()