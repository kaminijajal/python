a = int(input("Enter Value of A = "))
b = int(input("Enter Value of B = "))
print("Enter Any One ( + ,- ,*,/ )")
c = str(input("Enter sign =  "))

if c == '+':
    print("sum : ",(a+b))
elif c == '-':
    print("Sub : ",(a-b))
elif c == '*':
    print("Mul : ",(a*b))
elif c == '/':
    print("Div : ",(a/b))
else:
    print("Invalid Input")


