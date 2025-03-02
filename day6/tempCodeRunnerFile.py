text="""
1. Productivity
2. Time management
3. Communication"""
while True:
    user_action = input("type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        file = open("todos.txt", "r")
        todos = file.readlines()
        todos.append(todo)
        file.close()
        file = open("todos.txt", "w")
        file.writelines(todos)
        file.close()
    elif user_action.startswith("show"):
        file = open("todos.txt", "r")
        todos = file.readlines()
        file.close()
        for index, i in enumerate(todos):
            i = i.strip("\n")
            row = f"{index + 1} - {i}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1
            with open("todos.txt", "r") as file:
                todos = file.readlines()
            new_todo = input("Enter a new todo:")
            todos[number] = new_todo + "\n"
            with open("todos.txt", "w") as file:
                file.writelines(todos)
        except ValueError:
            print("command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            with open("todos.txt", "r") as file:
                todos = file.readlines()
            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)
            with open("todos.txt", "w") as file:
                file.writelines(todos)
            message = f"Todo{index} was removed from the list"
            print(message)
        except IndexError:
            print("Command is not valid")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid")
print("Bye")
