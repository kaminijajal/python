order = {}
def orderDetails():
    print("Order Booking:")
    name = input("Enter Your Name : ")
    type = input("Enter Device Type : ")
    issue = input("Enter Issue : ")
    date = input("Due date : ")
    order.update({"name":name,"type":type,"issue":issue,"date":date})
    print("Order book Sucessfully")
    # print(order)


def billing():
    print("Billing")
    partCost = int(input("Enter Part Cost : "))
    fee = int(input("Enter Ripering Fee : "))
    tax = 0.18
    discout = int(input("Enter Discount : "))

    total = partCost+fee
    taxrate = total*tax
    ftotal = total+taxrate-discout

    print("----------------invoice-----------------")
    print(f"Cusomer Name :{order['name']}")
    print(f"Type : {order['type']}")
    print(f"issue : {order['issue']}")
    print(f"PartCost : {partCost}")
    print(f"Repair Fee : {fee}")
    print(f"Gst Tax : {taxrate}")
    print(f"Discount : {discout}")
    print(f"Total Amount payable : {ftotal}")

cont = 'y'
while cont !='n':

    choice = int(input("""choose Number:
                    1.Order Booking
                    2. Billing
                    """))
    if choice == 1 :
        orderDetails()
    elif choice == 2:
        billing()
    else:
        print("Invalid choice")

    cont = input("do u want to continu? y or n")
