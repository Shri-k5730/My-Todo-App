def get_todos(filepath="D:/pythonProject/web_app1/todos.txt"):
    """ Read text file and return the todos in the file """
    with open(filepath,'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath="D:/pythonProject/web_app1/todos.txt"):
    """ Writes todos to the file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
