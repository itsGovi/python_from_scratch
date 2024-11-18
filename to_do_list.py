import json

class ToDoList:
    def __init__(self):
        try:
            with open('tasks.json', 'r') as file:
                self.tasks = json.load(file)
        except FileNotFoundError as e:
            self.tasks = []
            print(e)
        except json.JSONDecodeError as e:
            self.tasks = []
            print(e)
        while True:
            self.ask_input = input("What do you want to do? \n 1. View Current task(s) \n 2. Create new task \n 3.  Delete a task")
            if self.ask_input in ['1', '2', '3', 'quit', 'exit']:
                if self.ask_input == '1':
                    self.view_tasks()
                if self.ask_input == '2':
                    self.create_task()
                if self.ask_input == '3':
                    self.delete_task()
            elif self.ask_input in ['quit', 'exit']:
                break
            else:
                print("Invalid input, please try again")

    def view_tasks(self):
        try:
            if not self.tasks:
                raise ValueError ("The file is empty!")
            for task in self.tasks:
                print(task)
        except ValueError as e:
            print(e)