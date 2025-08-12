def add(a,b):
    sum = a+b
    print("Addition = ",sum)

def sub(a,b):
    s = a-b
    print("Subtraction = ",s)

def mul(a,b):
    m = a*b
    print("Multiplication = ",m)

def div(a,b):
    d = a/b 
    print("Division = ",d)

x = int(input("Enter Number : "))
y = int(input("Enter Number : "))

z = input("Any One operation choose (+ , - , * , /)")

if z == '+':
    add(x,y)
elif z == '-':
    sub(x,y)
elif z == '*':
    mul(x,y)
elif z == "/":
    div(x,y)
else:
    print("Invalid Input")