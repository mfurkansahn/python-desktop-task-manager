FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """
    Reads a text file and returns a list of todo items
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """
    Writes the todo items listed in the text file
    :param todos_arg:
    :param filepath:
    :return:
    """
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)


if __name__ == "functions":
    print(f"The messages come from {__name__}")
    # print(get_todos())

if __name__ == "__main__":
    print(f"The messages come from {__name__}")
    # print(get_todos())