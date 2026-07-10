# #dictionaries
# phone_no = {
#     'ram':1234,
#     'mohan':4444,
#     'nikhil':5555,
# }
# print(phone_no)
# print(phone_no['ram'])#this lines results the value for this code
# print(phone_no.pop('ram'))
# print(phone_no)
# phone_no['nikhil'] = 2828
# print(phone_no)

# print(phone_no.get('nikhil'))#this line gets the value safely without errors   
# #in dect it raises more errors so to avoid this while getting  the value we will use get function
# print("for loop using the dictionaries")
# for thing in phone_no:
#     print(thing)#this line of code returns the keys in the dictionarie
#     print(phone_no[thing])
# tekkali = 'Tekkali'
# my_list = {
#     "Tekkali":["Benarji","Karthik","Nikhil"],
#     "Srikakulam":["Deji","Nikhilesh"],
# }
# print(my_list[tekkali][1])

my_dictionarie={
    "nikhil":28,
    "nikhilesh":29,
    "deji":13
}
print(my_dictionarie["nikhil"])#accesing the value at the specified position

dictionarie = {
    28:"nikhil",
    13:"deji"
}
print(dictionarie)
dictionarie[48] = "benarji"  # benarji element is added to the dictionarie now
print(dictionarie.keys())
print(dictionarie)