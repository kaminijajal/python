# class Animal():
    # def __init__(self,id,name,color):
    #     print(id,name,color)

# a1 = Animal(1,"Cat","Black")

class Fruit():
    def __init__(self,id,name):
       
        self.id = id
        self.name = name
    
    def display(self):
        print(self.id,self.name)

    def test(self):
        print(self.id)

f1 = Fruit(1,"Apple")
f1.display()
f1.test()
    
