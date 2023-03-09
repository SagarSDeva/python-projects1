#pizza delivery Bill code
print("Welcome to SSD Pizza Delivery home")
Bill=0
print("Small Pizza: ₹99\nMedium Pizza: ₹159\nLarge Pizza: ₹199")
size = input("select size for your Pizza:press  S-small,M-medium,L-large ")
if(size=="S"):
    a=int(input("How many Small Pizza's Do you want?"))
    Bill = Bill+(a*99)
if(size=="M"):
    a=int(input("How many medium Pizza's Do you want?"))
    Bill = Bill+(a*159)
if(size=="L"):
    a=int(input("How many large Pizza's Do you want?"))
    Bill = Bill+(a*199)

print("Extra Toppings available:1-VEG:Black Olives,Crisp Capsicum,Paneer,Mushroom,Golden Corn,Fresh Tomato,Jalapeno,Red Pepper & Babycorn ₹35 for each\nNON-VEG:Barbeque Chicken-₹55,Hot 'n' Spicy Chicken-₹65,Chunky Chicken-₹65 and Chicken Salami-₹85\n Extra cheese for any size pizza is:Mozzarella,Pecorino,Parmesan and asiago cheese: ₹25 for any pizza\n")

choose = int(input("select Toppings:1-VEG,2-NON_VEG\n3-no toppings "))
Toppings_Veg = ["Black Olives","Crisp Capsicum","Paneer,Mushroom","Golden Corn","Fresh Tomato","Jalapeno","Red Pepper","Babycorn"]
Toppings_Non_Veg = ['Barbeque Chicken','Hot n Spicy Chicken','Chunky Chicken','Chicken Salami']
Extra_cheese = ["Mozzarella","Pecorino","Parmesan","asiago cheese"]
if(choose==1 or choose==2):
    if(choose==1):
        count= int(input("how many toppings you want to add"))
        veg2 = input("Black Olives,Crisp Capsicum,Paneer,Mushroom,Golden Corn,Fresh Tomato,Jalapeno,Red Pepper,Babycorn ").lower()
        Bill =Bill+(35*count)
    elif(choose==2):
        nonveg2=int(input("Barbeque Chicken-1,Hot 'n' Spicy Chicken-2,Chunky Chicken-3,Chicken Salami-4 "))
        if(nonveg2==1):
            Bill+=55
        elif nonveg2==2:
            Bill+=65
        elif nonveg2==3:
            Bill+=65
        elif nonveg2==4:
            Bill+=85
else:
    Bill=Bill
e=int(input("Do you want extra cheese type: 1-yes,3-no,"))
if e==1:
    Bill+=25
elif(e==3):
    Bill=Bill







else:
    print("Please choose from these options only: S-small\nM-medium\nL-large please press capital letters thank you")
#Discount Offer
if(Bill>=500):
    Bill-=35
    if(Bill>=850):
        Bill-=70
        if(Bill>=1000):
            Bill-=95
print(f"Your Total bill is: ₹{Bill}")

#

