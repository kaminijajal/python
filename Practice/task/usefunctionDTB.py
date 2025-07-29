def decimal(n):
    r = ""
    while n!=0:
        rem = n % 2
        r = str(rem)+r
        n //=2
    print(r)

decimal(105)
        