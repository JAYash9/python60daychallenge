# try:
#     total_value = float(input("Enter total value: "))
#     value = float(input("Enter value: "))

#     percentage = value / total_value * 100

#     print(f"That is {percentage} %")
# except ValueError:
#     print("You need to enter a number. Run the program again")
# Advanced error handling
# try:
#     total_value = float(input("Enter total value: "))
#     value = float(input("Enter value: "))

#     percentage = value / total_value * 100

#     print(f"That is {percentage}%")
# except ZeroDivisionError:
#     print("Your total value cannot be zero")
# i need help of chatgpt in this problem
filenames = ["report.txt", "downloads.txt", "success.txt", "folders.txt"]
for i in filenames:
    if i.endswith(".txt"):
        print(i[:-4])