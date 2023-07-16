FILEPATH = "../app1/files/todos.txt"

def get_todos(path=FILEPATH):
    """Read a text file and return list of todos"""
    with open(path, "r") as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(arg, path=FILEPATH):
    with open(path, "w") as file:
        file.writelines(arg)

if __name__ == "__main__":
    print("Hello")