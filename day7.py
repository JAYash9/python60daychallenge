#  lis comprehension
names = ["john smith", "jay santi", "eva kuki"]
names =[names.title() for names in names]
print(names)
# length and list comprehension
usernames = ["john 1990", "alberta1970", "magnola2000"]
new_list=[len(s) for s in usernames]
print(new_list)
# type conversion and list comprehension
user_entries = ['10', '19.1', '20']
new_list=[float(s) for s in user_entries]
print(new_list)
# list comprehension on numbers
numbers = [10, 20, 30]
new_list=[s*2 for s in numbers]
print(new_list)
#sum of numbers
user_entries = ['10', '19.1', '20']
new_list=[float(s) for s in user_entries]
# print(new_list)
res=sum(new_list)
print(res)
    