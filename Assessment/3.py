print("""
      Welcome to Fruit market
            1) Manager
            2) Customer""")


def fruit(rol):
    
    if rol == 1:
        print("""
            Fruit Manager market
               
            1)Add Fruit stock
            2)View Fruit Stock
            3)Update Fruit stock""")
    elif rol == 2:
        print("Customer")
    else:
        print("Invalid Role")
a = int(input("Select your rol : "))
fruit(a)

def manager(choice):
    if choice == 1:
        
        print("add")
    elif choice == 2:
        print("View")
    elif choice == 3:
        print("Update")
    else :
        print("Invalid")

m = int(input("Enter your Choice "))
manager(m)

def addFruit():
    print("Add Fruit stock")
    print("Enter fruit Name : ")
    print("Enter qty (in kg) : ")
    print("Enter Price : ")

addFruit()

