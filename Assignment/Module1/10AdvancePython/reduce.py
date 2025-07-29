from functools import reduce

l = [2,5,7,10,12]

def mul(x,y):
    # print(x,y)
    x = x*y
    return x

product = reduce(mul,l)

print(product)