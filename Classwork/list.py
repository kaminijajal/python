# l = [1,5,10,15,20,"abc",57.89,True]
# l = list((1,2,3))
# print(l)
# print(len(l))
# print(type(l))


#Access list item
# l = ["abc","efg","hij","klm","nop","qrst"]
# print(l[0])
# print(l[-1])
# print(l[3:])
# print(l[2:5])
# print(l[:6])
# print(l[::-1])


#change item value :
# l = [100,200,300,400,500,600]

# l[2] = 700
# l.insert(5,700)
# l.append(1000)

# l[1:3] = []

# l.extend("100")

# j = [10,20,30]
# l.extend(j)

# print(l)


#remove list item
# l = [1,2,3,4,5,6,7,8,9,10]

# l.remove(7)
# l.pop()
# l.pop(1)
# l.clear()
# del l
# print(l)



# l = ["j","k","l","m","n","o","p"]

# for i in l:
#     print(i)

# for i in range(len(l)):
#     print(l[i])

# i=0
# while i<len(l):
#     print(l[i])
#     i+=1


# l = ["table","pen","pencial","cutter","bord","duster"]

# for i in l:
#     if "p" in i:
#         print(i)


# a =  [i for i in l if "p" in i]
# a = [i for i in l if i.startswith("c")]

#l = [1060,15,25,25,30,11,35,40,50,]

# a = [i for i in l if i%2==0]
# print(a)

# l.sort()
# l.sort(reverse=True)
# l.reverse()
# print(l)

# a = l.copy()
# a = list(l)
# a = l[:]
# print(a)


# x = [10,20,30]
# y = [100,200,300]

# x.extend(y)
# i = x+y
# print(i)

# for i in y:
#     x.append(i)

# print(x)

# print(l.count(4))

# print(l.index(4))


l = ["grapes","banana","patato","brinjal"]

# newlist = [x for x in l]
# print(newlist)

for x in l:
    print("abc")

print("=================================")

newlist = ["abc" for x in l ]
print(newlist)