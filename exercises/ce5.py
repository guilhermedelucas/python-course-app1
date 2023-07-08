user_prompt = input('Enter a new member: ')

file = open('../files/members.txt', 'r')
members = file.readlines()
file.close()

members.append(user_prompt + '\n')
file = open('../files/members.txt', 'w')
file.writelines(members)
file.close()