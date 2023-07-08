todos = []

while True:
    user_action = input('Type add, show, edit, complete or exit: ')

    match user_action.strip():
        case 'add':
            todo = input('Enter a todo: ')
            todos.append(todo)
        case 'show' | 'display':
            for i, todo in enumerate(todos):
                print(f'{i + 1}-{todo.title()}')
            print()
        case 'edit':
            number = int(input('Number of todo to edit: '))
            number = number - 1
            new_todo = input('Enter new todo: ')
            todos[number] = new_todo
        case 'complete':
            number = int(input('Number of the todo to complete: '))
            todos.pop(number - 1)
        case 'exit':
            break
        case _:
            print('Hey, you entered an unknown command')

print('Bye')

hey = f'My first task is: {todos[0]}'
print(hey)