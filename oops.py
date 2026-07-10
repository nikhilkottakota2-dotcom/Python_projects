#oops in python
# class car:
#     Model="volvo"
#     color="red"
# c1 = car()
# print(c1.Model)
# print(c1.color)

# class student:
#     def greet(xyz):
#         print(xyz)
# s1 = student()
# print(s1)
# s1.greet()
# class car:
#     wheels = 4
#     def __init__(self,name,speed):#in python the constructor should have two unserscores
# #before and after the constructor

#         self.name = name
#         self.speed= speed

#     def display(self):
#         print(self.wheels)
#         print(self.name)
#         print(self.speed)

# c1 = car("BMW",200)
# c1.display()

# class bank:
#     def __init__(self):
#         self.__balance = 1000
#     def show_balance(self):
#         print(self.__balance)
#     def deposit(self,amount):
#         self.__balance += amount

# b = bank()

# b.show_balance()
# b.deposit(1000)
# print("Avaliable balance")
# b.show_balance()
# # b.__balance = 3000 value doesnt changed because it is encapsulated
# b.show_balance()

# class employee:
#     def work(self):
#         print("Employee is working")
# class developer(employee):
#     def develop(self):
#         print("Developer is developing the code")
# class tester(employee):
#     def employee(self):
#         print("tester is testing the code")

# d = developer()

# d.work()
# d.develop()

# from turtle import Turtle,Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from turtle import Turtle,Screen
my_turtle = Turtle()
print(my_turtle)
my_turtle.shape("turtle")
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.forward(100)
screen = Screen()
print(screen.canvheight)