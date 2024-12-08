FILEPATH = 'todos.txt'

def get_todos(filepath=FILEPATH):
    """ Read a text file and return the
    list of to-do items
    """  # docstrings
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


# print(help(get_todos))

def write_todos(todos_arg, filepath=FILEPATH):
    """Write the to-do items in the text file."""
    with open("todos.txt", "w") as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello!")
    print(__name__)



