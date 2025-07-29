 #   * 
 #  * *  
 # * * * 
 #  * *  
 #   *   
for i in range(3):
    for k in range(3-i):
        print(" ",end="")
    for j in range(i+1):
        print("* ",end="")
    print()
for a in range(2,0,-1):
    for b in range(3-a):
        print(" ",end="")
    for c in range(a):
        print(" *",end="")
    print()