def get_todos(filepath='todo_list.txt'):
    """
    Reads a text file and returns a list
    of to-do items
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath='todo_list.txt'):
    """
    Writes new items to the to-do list text file
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)