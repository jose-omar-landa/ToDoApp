while True:
    user_action = input("Type add, show, edit, complete, or exit: ""Type add, show, or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter an item for your todo list: ") + "\n"

            with open('todo_list.txt', "r") as file:
                todos = file.readlines()

            todos.append(todo.title())

            with open('todo_list.txt', 'w') as file:
                file.writelines(todos)

            print("Item added!")

        case "show":

            with open('todo_list.txt', "r") as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip("\n")
                row = f"{index + 1}. {item}"
                print(row)
        case "edit":
            todo_item_num = int(input("Enter the todo list item number you'd like to edit: "))
            todo_item_num = todo_item_num - 1

            with open('todo_list.txt', "r") as file:
                todos = file.readlines()

            new_item = input("Enter a new todo list item: ")
            todos[todo_item_num] = new_item.title() + "\n"
            print("Item edited.")

            with open('todo_list.txt', 'w') as file:
                file.writelines(todos)

            with open('todo_list.txt', "r") as file:
                todos = file.readlines()

            print("Todo list is now: ")
            for index, item in enumerate(todos):
                item = item.strip("\n")
                row = f"{index + 1}. {item}"
                print(row)

        case "complete":
            list_item_num = int(input("Enter the todo list item number you'd like to complete: "))

            with open('todo_list.txt', "r") as file:
                todos = file.readlines()

            todos.pop(list_item_num - 1)

            with open('todo_list.txt', 'w') as file:
                file.writelines(todos)

            print("Item completed!")

            with open('todo_list.txt', "r") as file:
                todos = file.readlines()

            print("Todo list is now: ")
            for index, item in enumerate(todos):
                item = item.strip("\n")
                row = f"{index + 1}. {item}"
                print(row)

        case "exit":
            print("Goodbye!")
            break


