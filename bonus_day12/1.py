# def strength(password):
#     if len(password) >= 8 and any(i.isdigit() for i in password) and any(i.isupper() for i in password):
#         return "Strong Password"
#     else:
#         return "Weak Password"
# def Average(args):
#     return sum(args) / len(args)
# person=input("Enter your name: ")
# def greet(person):
#     print(f"Hi {person}")
# greet("lisa")
# def concat(string1,string2):
#     string3=string1+string2
#     return string3
# print(concat("Hello","World"))
def greet(name):
    names=name.capitalize()
    return f"Hi {names}"
print(greet("john"))