import functions
import time


now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is now", now)

while True:
    text_input = input("Type add, show, complete, edit or exit:").strip()

    if text_input.startswith('add'):
        todo = text_input[4:]

        todos = functions.get_todos()
        todos.append(todo.title() + "\n")

        functions.write_todos(todos)

    elif text_input.startswith('show'):
        todos = functions.get_todos()
        new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(new_todos):
            print(f"{index + 1}. {item.title()}")
    elif text_input.startswith('edit'):
        try:
            number = int(text_input[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + "\n"

            functions.write_todos(todos)
        except ValueError:
            print("Invalid command.")
            continue
    elif text_input.startswith('complete'):
        try:
            number = int(text_input[9:])

            todos = functions.get_todos()

            item_to_be_removed = todos[number - 1].strip("\n")

            todos.pop(number - 1)

            functions.write_todos(todos)
            print(f'Todo "{item_to_be_removed}" was removed from the list.')
        except IndexError:
            print("There is no item with in the list with that number")

    elif text_input in 'exit':
        break

    else:
        print("Command is invalid")
print("Bye")
