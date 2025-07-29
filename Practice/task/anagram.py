a = input("Enter a sentence ")
b = input("Enter a sentence ")



x = sorted(a.replace(" ","")) 
y = sorted(b.replace(" ",""))

#x = sorted(a)
#y = sorted(b)

#spaceremovea = a.replace(" ","")
#spaceremoveb = b.replace(" ","")

if x == y:
    print("anagram")
else :
    print("Not anagram") 

#print(x)
#print(y)