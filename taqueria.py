#Dictionary: key is item name and value is price in $

menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

#keeps the runnimg total of the order
total = 0

#Loop: keeps asking for items until control-d is pressed
while True:
    try:
        item = input("Item: ").title()  #asks for an item and coverts it to title case (eg. taco->Taco)
    except EOFError: #control-d raises an EOFError
        print() #print a new line so it doesnt stay stuck in the "Item:" prompt
        break #exits the loop

    if item in menu: #only adds price if the item is in the menu
        total += menu[item] #add the item price to the total
        print(f"Total: ${total:.2f}") #show total with $ and two decimal places (eg. $22.50)

