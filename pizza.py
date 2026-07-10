#pizza billing system
a = input("Enter the size of the pizza S,M or L")
a = a.lower();
b = input("Pizza with extra cheese y/n")
if a == 's':
    if b == 'y':
        print("Your Bill is ₹130")
    else:
        print("Your bill is ₹100")
elif a == 'm':
    if b == 'y':
        print("your bill is ₹150")
    else:
        print("Your bill is ₹190")
else:
    if b == 'y':
        print("Your bill is ₹200")
    else:
        print("Your bill is ₹250")

print("----Thank You for choosing Pizza Hub")