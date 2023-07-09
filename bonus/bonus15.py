import json

with open('./files/questions.json', 'r') as file:
    data = json.load(file)

# data = json.loads(content)

score = 0
correct_answers = 0
incorrect_answers = 0

for question in data:
    # Print the question
    print(question['question_text'])
    for i, alternative in enumerate(question['alternatives']):
        print(f'{i + 1} - {alternative}')

    # Get user answer
    user_choice = int(input('Enter your answer: '))
    question['user_choice'] = user_choice


for i, question in enumerate(data):
    if question['user_choice'] == question['correct_answer']:
        score = score + 1
        result = 'Correct answer'
    else:
        result = 'Wrong answer'
    message = f"{result} {i+ 1} - Your answer: {question['user_choice']}, " \
              f"Correct answer: {question['correct_answer']}"
    print(message)

print(f'{score}/{len(data)}')