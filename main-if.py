def get_todos(filepath):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(filepath, content):
    with open(filepath, 'w') as file_local:
        file_local.writelines(content)

while True:
    # Get user input
    user_action = input('Type add, show, edit, complete or exit: ')

    # Strip white spaces from the input
    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos('files/todos.txt')
        todos.append(todo + '\n')

        write_todos('files/todos.txt', todos)
    elif user_action.startswith('show'):
        todos = get_todos('files/todos.txt')
        # inline loop
        # new_todos = [item.strip('\n') for item in todos]
        for i, todo in enumerate(todos):
            todo = todo.strip('\n')
            row = f'{i + 1}-{todo.title()}'
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:]) - 1

            todos = get_todos('files/todos.txt')
            new_todo = input('Enter new todo: ')
            todos[number] = new_todo + '\n'

            write_todos('files/todos.txt', todos)
        except ValueError:
            print('Your command is not valid.')
            continue
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:]) - 1

            todos = get_todos('files/todos.txt')
            todo_to_remove = todos[number].strip('\n')
            todos.pop(number)
            write_todos('files/todos.txt', todos)

            print(f'Todo {todo_to_remove} was removed from the list.')
        except (IndexError, ValueError):
            print('There\'s no item with that number.')
            continue
    elif user_action.startswith('exit'):
        break
    else:
        print('Hey, you entered an unknown command')

print('Bye')