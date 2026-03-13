from datetime import datetime

todo_items = []

while True:
    todo = input("Enter your to-do items for today. Type 'done' to save and exit.")
    if todo == 'done':
        break
    todo_items.append(todo)

content = "\n".join(todo_items)

day = datetime.now().strftime("%A")
filename = f'{day}.txt'
with open(filename, 'w') as f:
    f.write(content)

print(f'Your todo list was saved to {filename}')