import os

DOCUMENTS_DIR = os.path.join(os.path.expanduser("~"), "Documents")
APP_DIR = os.path.join(DOCUMENTS_DIR, "MyToDoApp")
FILEPATH = os.path.join(APP_DIR, "todos.txt")

if not os.path.exists(APP_DIR):
    os.makedirs(APP_DIR)

if not os.path.exists(FILEPATH):
    with open(FILEPATH, "w", encoding="utf-8"):
        pass


def get_todos(filepath=FILEPATH):
    with open(filepath, "r", encoding="utf-8") as file:
        return file.readlines()


def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, "w", encoding="utf-8") as file:
        file.writelines(todos_arg)

if __name__ == "functions":
    print(f"The messages come from {__name__}")
    # print(get_todos())

if __name__ == "__main__":
    print(f"The messages come from {__name__}")
    # print(get_todos())