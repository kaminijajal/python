for number in range(100,1000) :
    temp = number
    count = 0
    n = number
    while n != 0:
        #number%10
        n //=10
        count += 1

    sum = 0
    n = number 
    while n !=0:
        rem = n%10
        sum += pow(rem,count)
        n //=10
    if number == sum:
        print(f"{number} is armstrong")
