while True:
    user_action=input("type add ,show,edit ,complete or edit :")
    user_action=user_action.strip()
    match user_action:
        case 'add':
            todo=input("enter a todo:") +"\n"
            file=open('todos.txt','r')
            
            todos= file.readlines()
            todos.append(todo)
            file.close()
            file=open('todos.txt','w')
            file.writelines(todos)
            file.close()
        case 'show':
            file=open('todos.txt','r')
           
            
            todos= file.readlines()
            file.close()
            for index, i in enumerate(todos):
                i = i.strip('\n')
                row = f"{index + 1} - {i}"
                print(row)
        case 'edit':
            number=int(input("number of the todo to edit it"))
            number = number -1
            new_todo=input("Enter a new todo:")
            todos[number]=new_todo
        case 'exit':
            break