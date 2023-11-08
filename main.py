def get_todos(filepath):
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(filepath, todos_arg):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


while True:
    user_action = input("Type add, show, edit, complete, or exit: ""Type add, show, or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos('todo_list.txt')

        todos.append(todo.title() + '\n')

        write_todos('todo_list.txt', todos)

        print("Item added!")

    elif user_action.startswith("show"):

        todos = get_todos('todo_list.txt')

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}. {item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            todo_item_num = int(user_action[5:])
            todo_item_num = todo_item_num - 1

            todos = get_todos('todo_list.txt')

            new_item = input("Enter a new todo list item: ")
            todos[todo_item_num] = new_item.title() + "\n"
            print("Item edited.")

            write_todos('todo_list.txt', todos)

            todos = get_todos('todo_list.txt')

            print("Todo list is now: ")
            for index, item in enumerate(todos):
                item = item.strip("\n")
                row = f"{index + 1}. {item}"
                print(row)

        except ValueError:
            print("Input not valid. Please enter the todo item number to edit.")

    elif user_action.startswith("complete"):
        try:
            list_item_num = int(user_action[9:])

            todos = get_todos('todo_list.txt')

            todos.pop(list_item_num - 1)

            write_todos('todo_list.txt', todos)

            print("Item completed!")

            todos = get_todos('todo_list.txt')

            print("Todo list is now: ")
            for index, item in enumerate(todos):
                item = item.strip("\n")
                row = f"{index + 1}. {item}"
                print(row)

        except ValueError:
            print("Input not valid. Please enter the todo item number to complete.")

    elif user_action.startswith("exit"):
        print("Goodbye!")
        break

    else:
        print("Input is invalid, please enter a valid command!")


