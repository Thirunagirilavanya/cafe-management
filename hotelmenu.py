#DEfine the menu of Restaurant
menu = {
    'pizza':40,
    'pasta':50,
    'burger':60,
    'coffee':80,
    'salad':70,
}

#Greet
print("Welcome to Honey Restaurant")
print("pizza: Rs40\npasta: Rs5o\nburger: Rs60\nsalad: Rs70\ncoffee: Rs80\n")

order_total = 0
#80 + 70 = 150
item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1] #0 + 50
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Ordered item {item_1} is not available yet")
another_order = input("Do you want to add another item? (Yes/No) ")
if another_order == "Yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"Ordered item {item_2} is not available!") 
another_order = input("Do you want to add another item? (Yes/No) ")
if another_order == "Yes":
    item_3 = input("Enter the name of third item = ")
    if item_3 in menu:
        order_total += menu[item_3]
        print(f"Item {item_3} has been added to order")
    else:
        print(f"Ordered item {item_3} is not available!")                   
print(f"The total amount of items to pay is {order_total}")


