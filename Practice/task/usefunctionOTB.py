def octal(n):
    rem = ''
    while n > 0:
        rem = str(n % 8) + rem
        n //= 8
    print(rem)
octal(46)
        