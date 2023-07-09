from files import get_todos, write_todos

while True:
    # Get user input
    user_action = input('Type add, show, edit, complete or exit: ')

    # Strip white spaces from the input
    match user_action.strip():
        case 'add':
            todo = input('Enter a todo: ') + "\n"

            todos = get_todos()

            todos.append(todo)

            write_todos(todos)
        case 'show' | 'display':
            todos = get_todos()
            # inline loop
            # new_todos = [item.strip('\n') for item in todos]

            for i, todo in enumerate(todos):
                todo = todo.strip('\n')
                row = f'{i + 1}-{todo.title()}'
                print(row)
        case 'edit':
            number = int(input('Number of todo to edit: '))
            number = number - 1

            todos = get_todos()
            new_todo = input('Enter new todo: ')
            todos[number] = new_todo + '\n'

            write_todos(todos)
        case 'complete':
            number = int(input('Number of the todo to complete: '))

            todos = get_todos()
            todo_to_remove = todos[number - 1].strip('\n')
            todos.pop(number - 1)
            write_todos(todos)

            print(f'Todo {todo_to_remove} was removed from the list.')
        case 'exit':
            break
        case _:
            print('Hey, you entered an unknown command')

print('Bye')