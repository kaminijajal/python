a = int(input("Enter Aa Number"))

rem = ''
while a > 0:
    rem = str(a % 8) + rem
    a //= 8
print(rem)