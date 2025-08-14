s = "Hello Python"
    count = {}

    for i in s:
        if count.get(i) is None:
            count.update({i:1})
        else:
            k = count.get(i)
            k+=1
            count.update({i:k})
    print(count)