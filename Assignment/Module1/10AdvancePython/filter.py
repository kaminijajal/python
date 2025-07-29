

l = [1,3,2,4,6,10,11,23,54,67,77]

def even(n):
    if n%2==0:
        return n

list1 = filter(even,l)
print(list(list1))