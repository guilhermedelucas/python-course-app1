# Check for a password strength

password = input('Enter a new password: ')

result = {}

# Check password length
result['length'] = len(password) >= 8

digit = False
upper = False

for i in password:
    if i.isdigit():
        digit = True
    if i.isupper():
        upper = True

result['digits'] = digit
result['upper'] = upper

print(result)
print(result.values())
print(result.keys())

# all checks if all elements of the list is True
if all(result.values()):
    print('Strong password')
else:
    print('Weak password')