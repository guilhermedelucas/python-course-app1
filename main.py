todos = []

while True:
    # Get user input
    user_action = input('Type add, show, edit, complete or exit: ')

    # Strip white spaces from the input
    match user_action.strip():
        case 'add':
            todo = input('Enter a todo: ') + "\n"

            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('files/todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'show' | 'display':
            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()

            # inline loop
            # new_todos = [item.strip('\n') for item in todos]

            for i, todo in enumerate(todos):
                todo = todo.strip('\n')
                row = f'{i + 1}-{todo.title()}'
                print(row)
        case 'edit':
            file = open('files/todos.txt', 'r')
            number = int(input('Number of todo to edit: '))
            number = number - 1
            new_todo = input('Enter new todo: ') + '\n'
            todos[number] = new_todo
        case 'complete':
            number = int(input('Number of the todo to complete: '))

            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.pop(number - 1)
            file = open('files/todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'exit':
            break
        case _:
            print('Hey, you entered an unknown command')

print('Bye')

hey = f'My first task is: {todos[0]}'
print(hey)