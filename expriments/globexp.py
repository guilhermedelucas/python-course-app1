import glob
myFiles = glob.glob('../files/*.txt')

for filepath in myFiles:
    print(filepath)
    with open(filepath, 'r') as file:
        print(file.read())