def library_ascii_art():
    art = r"""
 __        __   _                            _             
 \ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___        
  \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \       
   \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) |      
    \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/       
                                                            
  _       _ _                 __  __                                           
 | |     (_) |               |  \/  |                                        
 | |      _| |__  _ __ __ _  | \  / | __ _ _ __   __ _  __ _  ___ _ __   
 | |     | | '_ \| '__/ _` | | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__/   
 | |____ | | |_) | | | (_| | | |  | | (_| | | | | (_| | (_| |  __/ |  
 |______||_|_.__/|_|  \__,_| |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_| 
                                                       __/ |                       
                                                      |___/                        
    """
    print(art)

# Call the function
library_ascii_art()

#Library management system
books = {
    "arjun":10,
    "harry potter":15,
    "shiva the codex":10,
    "psychology of money":20
}
program_continue = "y"
while program_continue == "y":

#books printing 
    print("_______________________________________________")
    for key,value in books.items():
        print(key + ":" + str(value))
    #avaliable books
    #books accessing 
    print("_______________________________________________")
    choice = input("Do you want to return_back or borrow the book:").lower()
    if choice == "return_back":
        # print("Book return function")
        book_choice = input("Print Enter the book name:")
        if book_choice in books:
            books[book_choice] += 1
            print("Book is returned")
            program_continue = input("Do you want any other books (y/n)").lower()
        print("_______________________________________________")
    elif choice == "borrow":
    # print("Book borrow function")
        book_choice = input("Print Enter the book name:")
        if book_choice in books:
            if books[book_choice] >= 1:
                print("Book is avaliable")

                books[book_choice] -= 1
                print("Book is borrowed")
                program_continue = input("Do you want any other books (y/n)").lower()
                print("_______________________________________________")
            else:
                print(f"{book_choice} is not avaliable right now")
                program_continue = input("Do you want any other books (y/n)").lower()
                print("_______________________________________________")
        else:
            print("There is a typo error or we dont have that books")
            program_continue = input("Do you want any other books (y/n)").lower()
            print("_______________________________________________")
    elif choice == "avaliable":
        for key,value in books.items():
            print(key + ":" + str(value))
        program_continue = input("Do you want any other books (y/n)").lower()
        print("_______________________________________________")
    else:
        print("Wrong Entry")
        program_continue = input("Do you want any other books (y/n)").lower()
    print("_______________________________________________")
    