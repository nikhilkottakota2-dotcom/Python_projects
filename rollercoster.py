# Rollercoaster Ticket Manager
photographer = 50
height = int(input("Enter Your Height (in cm): "))

if height >= 120:
    age = int(input("Enter Your Age: "))
    
    if age <= 10:
        ticket = 20
        print("The ticket for children is ₹20")
    elif age <= 20:   # no need to check age >= 10 again
        ticket = 40
        print("The ticket for teenagers is ₹40")
    else:
        ticket = 60
        print("The ticket for adults is ₹60")
        
    photo = input("Do you want a photographer for this amusement park journey? (y/n): ")
    
    print("\n------ Your Bill ------")
    if photo.lower() == 'y':
        print(f"The photographer charge    = ₹{photographer}")
        print(f"Your ticket Price          = ₹{ticket}")
        total = photographer + ticket
        print(f"The total ticket price is  = ₹{total}")
    else:
        print(f"The Total ticket price is  = ₹{ticket}")

else:
    print("Sorry, you should be taller than 120 cm to ride.")
