todos = []

while True:
    # Get user input
    user_action = input('Type add, show, edit, complete or exit: ')

    # Strip white spaces from the input
    match user_action.strip():
        case 'add':
            todo = input('Enter a todo: ') + "\n"

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)
        case 'show' | 'display':
            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            # inline loop
            # new_todos = [item.strip('\n') for item in todos]

            for i, todo in enumerate(todos):
                todo = todo.strip('\n')
                row = f'{i + 1}-{todo.title()}'
                print(row)
        case 'edit':
            number = int(input('Number of todo to edit: '))
            number = number - 1

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input('Enter new todo: ')
            todos[number] = new_todo + '\n'

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)
        case 'complete':
            number = int(input('Number of the todo to complete: '))

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()
            todo_to_remove = todos[number - 1].strip('\n')
            todos.pop(number - 1)
            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

            print(f'Todo {todo_to_remove} was removed from the list.')
        case 'exit':
            break
        case _:
            print('Hey, you entered an unknown command')

print('Bye')