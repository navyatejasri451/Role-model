from datetime import datetime
name=input("enter your name:")
lists="""
Rice   :   60/kg
Sugar  :   45/kg
Colgate:   80/each
Paneer :   110/kg
Soaps  :   100/each
Yipee  :   80/kg
Salt   :   50/kg
Flour  :   70/kg
"""
print(lists)

#Declarations
price = 0
pricelist = []
totalprice=0
finalprice=0
ilist=[]#list of items
qlist=[]#list of quantity
items={
"Rice"   :   60,
"Sugar"  :   45,
"Colgate":   80,
"Paneer" :   110,
"Soaps"  :   100,
"Yipee"  :   80,
"Salt"   :   50,
"Flour"  :   70
}
#Assiging some options:
option=int(input("to display list of items press1..."))
if option ==1:
    print(lists)
    for i in range(len(items)):
        inp1=int(input("If u wanna buy items press1 or else press2"))
        if inp1==2:
            break
        if inp1==1:
            item=input("Enter your items..")
            quantity=int(input("Enter your Quantity..."))
            #calculation:
            if item in items.key():
                price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
#print(price)
 #Bill for Group of items
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("Sorry The selected item is not available...")
    else:
        print("You entered wrong number...")
#generating the Bill
inp=input("can i bill the items yes or no....")
if inp=='yes':
    pass
if finalamount!=0:
    print(25*" = ","satya supermarket", 25*"=")
    print(28*" ","Rajahmundry")
    print("Name:", name,30*" ","Date:", datetime.now())
    print(75*"-")
    print("sno",8*" ",'items', 8*" ",'Quantity', 3*" ", 'price')
    for i in range(len(pricelist)):
            print(i,8*" ",8*" ",ilist[i],3*" ",qlist[i],plist[i])
print(50*" ",'TotalAmount:', 'Rs',totalprice)
print("gst amount", 50*" ",'Rs',gst)
print(75*"-")
print(50*" ",'FinalAmount:', 'Rs',finalprice)
print(75*"-")
print(50*" ","Thanks for Visiting")
print(75*"-")


