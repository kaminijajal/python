from multipledispatch import dispatch

class clac:
    # @dispatch(int,int)
    # def add(self,x,y):
    #     print(f"addition is {x+y}")

    # @dispatch(int, int, int)
    # def add(self,x,y,z):
    #     print(f"Addition id {x+y+z}")

    def add(self,*a):
        sum = 0
        for i in a:
            sum +=i
        print(sum)


c1 = clac
c1.add(5,10,1000)
c1.add(1,2,3,4,5,6)
