filenames = ['a.txt', 'b.txt', 'c.txt']

for filename in filenames:
    file = open(f'../files/{filename}')
    print(file.read())
    file.close()