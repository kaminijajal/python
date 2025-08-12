f = open("user.txt",'w')
f.write("Hello Python\n")
f.close()

f = open("user.txt",'a')
f.writelines("Welcome")
f.close()

f = open("user.txt",'r')
data = f.readlines()
#print(data)

print(data.find("python"))
