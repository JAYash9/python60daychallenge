# date = input("enter user a date")
# mood = input("how do you rate yourself from 1 to 10")
# thoughts = input("enter your thoughts\n")
# with open(f"{date}.txt", "x") as file:
#     file.write(f"Mood: {mood}\n")
#     file.write(f"Journal: {thoughts}\n")
#     print("journal entry saved")
# languages = ['English', 'German', 'Spanish']
# for i in languages:
    
#     with open(f"{i}.txt","x") as file:
#         file.write(f"{i}")
with open("story.txt","r") as file:
    todos=file.read()
with open("story_copy.txt","w")as file:
    file.write(todos)


