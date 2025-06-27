for number in range(1,101) :
    if number < 2:
        print(f"{number} Not rime")
        continue
    flag = 0
    for i in range(2,number):
        if number % i == 0:
            flag = 1
            break
    if flag == 0:
        print(f"{number} Prime")
    else:
        print(f"{number} Not Prime")