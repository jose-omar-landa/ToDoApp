from modules import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print(now)

while True:
    user_action = input("Type add, show, edit, complete, or exit: ""Type add, show, or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo.title() + '\n')

        functions.write_todos(todos)

        print("Item added!")

    elif user_action.startswith("show"):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}. {item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            todo_item_num = int(user_action[5:])
            todo_item_num = todo_item_num - 1

            todos = functions.get_todos()

            new_item = input("Enter a new todo list item: ")
            todos[todo_item_num] = new_item.title() + "\n"
            print("Item edited.")

            functions.write_todos(todos)

            todos = functions.get_todos()

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

            todos = functions.get_todos()

            todos.pop(list_item_num - 1)

            functions.write_todos(todos)

            print("Item completed!")

            todos = functions.get_todos()

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


