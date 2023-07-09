from bonus.parsers14 import parse
from bonus.converters14 import convert

feet_inches = input('Enter feet and inches: ')

parsed = parse(feet_inches)
feet = parsed['feet']
inches = parsed['inches']
result = convert(feet, inches)

print(f"{feet} fett and {inches} is equal to {result}")

if result < 1:
    print('Kid is too small.')
else:
    print('Kid can use the slide')