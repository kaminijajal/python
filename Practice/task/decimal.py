a = int(input("Enter Aa Number"))


rem = ''
while a > 0:
    rem = str(a % 10) + rem
    a //= 10
print(rem)