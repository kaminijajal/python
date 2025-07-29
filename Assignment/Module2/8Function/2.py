def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

x = int(input("Enter Number : "))
y = int(input("Enter Number : "))
z = input("Enter choice ( + , - , * , / ) : ")

if z == '+':
    print("Addtion",add(x,y))
elif z == '-':
    print("Subtraction",sub(x,y))
elif z == '*':
    print("Multiplation",mul(x,y))
elif z == '/':
    print("Division",div(x,y))
else:
    print("Invalid Choice")
