feet_inches = input('Enter feet and inches: ')

def parse(feet_inches_arg):
    parts = feet_inches_arg.split(' ')
    feet_local = float(parts[0])
    inches_local = float(parts[1])
    return {"feet": feet_local, "inches": inches_local}


def convert(feet_local, inches_local):
    return feet_local * 0.3048 + inches_local * 0.0254


parsed = parse(feet_inches)
feet = parsed['feet']
inches = parsed['inches']
result = convert(feet, inches)

print(f"{feet} fett and {inches} is equal to {result}")

if result < 1:
    print('Kid is too small.')
else:
    print('Kid can use the slide')