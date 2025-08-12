# f = open("user1.txt",'a')
# f.write("hello python\n")
# f.close()

f = open("user1.txt",'r')
data = f.readlines()
print(data)

# print(len(f))
l = data[0]
length = len(l)
print(length)