# default open function is 'r' (read)
with open('../files/doc.txt') as file:
    print(file.read())