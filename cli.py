from modules.files import get_todos, write_todos
import time

now = time.strftime('%b %d, %Y, %H:%M:%S')
print('It\'s', now)

while True:
    # Get user input
    user_action = input('Type add, show, edit, complete or exit: ')

    # Strip white spaces from the input
    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos()
        todos.append(todo + '\n')

        write_todos(todos)
    elif user_action.startswith('show'):
        todos = get_todos()
        # inline loop
        # new_todos = [item.strip('\n') for item in todos]
        for i, todo in enumerate(todos):
            todo = todo.strip('\n')
            row = f'{i + 1}-{todo.title()}'
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:]) - 1

            todos = get_todos()
            new_todo = input('Enter new todo: ')
            todos[number] = new_todo + '\n'

            write_todos(todos)
        except ValueError:
            print('Your command is not valid.')
            continue
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:]) - 1

            todos = get_todos()
            todo_to_remove = todos[number].strip('\n')
            todos.pop(number)
            write_todos(todos)

            print(f'Todo {todo_to_remove} was removed from the list.')
        except (IndexError, ValueError):
            print('There\'s no item with that number.')
            continue
    elif user_action.startswith('exit'):
        break
    else:
        print('Hey, you entered an unknown command')

print('Bye')