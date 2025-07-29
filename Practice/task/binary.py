a = int(input("Enter Aa Number"))

rem = ''
#for i in range(a):
while a > 0:
    rem = str(a % 2) + rem
    a //= 2
print(rem)