FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """
    Longer commenting stuff
    :param filepath:
    :return:
    """
    # read file (better method)
    with open(filepath, 'r') as file_Local:
        todos_local = file_Local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

# FOR TESTING!!!!
# how to run code when only when running this python file directly
#       (not if an import)
if __name__ == "__main__":
    print(get_todos())