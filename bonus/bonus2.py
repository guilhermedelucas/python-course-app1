password_prompt = 'Enter password: '
password = input(password_prompt)

while password != 'pass123':
    password = input(password_prompt)

print('Password was correct!')
