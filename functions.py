FILEPATH = "todos.txt"      # this is  variable though it acts like a constant


def get_todos(file_path=FILEPATH):   # Making file_path  a default argument by supplying default value for it
    """ Function reads a text file and returns list of todo items """
    with open(file_path, "r") as file_todo:
        todos_local = file_todo.readlines()  # dont need to close file now, it happens automatically
    return todos_local


def write_todos(todos_arg, filepath_arg=FILEPATH):
    """ Function writes list of todos to a text file """
    with open(filepath_arg, 'w') as file_again:
        file_again.writelines(todos_arg)


# print(__name__)

if __name__ == "__main__":
    print("I am inside functions")      # this is executed only when you run this functions14.py and not the cmdLineInter.py where its imported.

"""
___name___ is one of the default variables available to the program. When the you run functions14.py file, __name__ = __main__
Otherwise, when you run other file cmdLineInter.py, then its "functions"
"""