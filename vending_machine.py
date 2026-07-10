def vending_machine_ascii():
    art = r"""
    _______________________
   |                       |
   |   [  VENDING  ]       |
   |   [  MACHINE  ]       |
   |-----------------------|
   |  [ 1 ]  [ 2 ]  [ 3 ]  |
   |  [ A ]  [ B ]  [ C ]  |
   |  [ D ]  [ E ]  [ F ]  |
   |-----------------------|
   |   (   COINS SLOT   )  |
   |   (   NOTES SLOT   )  |
   |-----------------------|
   |   [   DISPENSE BOX  ] |
   |_______________________|
    """
    print(art)

vending_machine_ascii()

#vending machine
#todo adding the items 
item = {
    "pringles":{"Quantity":10,"price":80},
    "thumsup":{"Quantity":10,"price":50},
    "bingo":{"Quantity":10,"price":40},
    "lays":{"Quantity":10,"price":40},
    "cococola":{"Quantity":10,"price":60},
}

#todo coin management
def coin_manager(inserted_coins):
    if inserted_coins > item[choice]["price"]:
        exchange = inserted_coins - item[choice]["price"]
        print(f"You paid extra for this and here is your return amount{exchange}")
    elif inserted_coins == item[choice]["price"]:
        print("The amount is enough for the snack you want")
    else:
        print("You can't get the drink")
loop = "y"
# print(item["Pringles"])
while loop == "y":
    for keys,values in item.items():
        print(keys +":"+ str(values["price"]))
    choice = input("Enter the snack you want:").lower()
    if choice in item:
        print("You entered drink is avaliable")
        inserted_coins = int(input("Enter the coins:"))
        coin_manager(inserted_coins)
        item[choice]["Quantity"] -= 1
        loop = input("Enter do you want any other want (y/n):")
        print("_______________________________________________________")
    elif choice == "resource":
        print("_______________________________________________________")
        for keys,values in item.items():
            print(keys +":"+ str(values["Quantity"]))
        print("_______________________________________________________")
    else:
        print("You entered drink is not there in the vending machine")
        loop = input("Enter do you want any other want (y/n)")