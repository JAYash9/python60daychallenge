password=input("Enter the password:")
result={}

if len(password)>=8:
    result["length"]=True
else:
    result["length"]=False
digit=False
for i in password:
    if i.isdigit():
        digit=True
result["digits"]=digit
uppercase=False
for i in password:
    if i.isupper():
        uppercase=True
result["uppercase"]=uppercase
print(result)
# result.values it gives us the value of dictionary
if all(result.values()):
    print("Password is strong")
else:
    print("Password is weak")


