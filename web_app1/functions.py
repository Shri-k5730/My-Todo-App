def get_todos(filepath="web_app1/todos.txt"):
    """ Read text file and return the todos in the file """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="web_app1/todos.txt"):
    """ Writes todos to the file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


def get_user(filepath="web_app1/userlog.txt"):
    """ Read text file and return the todos in the file """
    with open(filepath, 'r') as file_local:
        user_local = file_local.readlines()
    return user_local


def write_user(users, filepath="web_app1/userlog.txt"):
    """ Writes todos to the file"""
    with open(filepath, 'w') as file:
        file.writelines(users)