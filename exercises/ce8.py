def strength(password):
    result = {'length': len(password) >= 8}

    for character in password:
        if character.isdigit():
            result['digit'] = True
        if character.isupper():
            result['upper'] = True

    if not all(result.values()):
        return 'Weak Password'
    return 'Strong Password'

print(strength('JJaaa888adsdaosdjasodij'))