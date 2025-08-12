f = open("data2.txt",'w')
f.write("Hello , How are you")
f.close()

f = open("data2.txt",'r')
data = f.read()
print(data)

