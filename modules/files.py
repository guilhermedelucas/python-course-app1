FILEPATH = 'files/todos.txt'


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(content, filepath=FILEPATH):
    """ Write the to-do items list in the text file """
    with open(filepath, 'w') as file_local:
        file_local.writelines(content)


if __name__ == '__main__':
    print('Hello')
    print(get_todos())