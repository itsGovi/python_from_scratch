import json

class ToDoList:
    def __init__(self):
        try:
            with open('tasks.json', 'r') as file:
                self.tasks = json.load(file)
        except FileNotFoundError as e:
            self.tasks = {}
            print(e)
        except json.JSONDecodeError as e:
            self.tasks = {}
            print(e)
        while True:
            self.ask_input = input("What do you want to do? \n 1. Create new task \n 2. View Current task(s) \n 3.  Delete a task")
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

    def create_task(self):
        try:
            task_title = input("What's the name of the task? ")
            while not task_title.strip(): # validate that it's not just empty or spaces
                print("The title can't just be empty or spaces")
                task_title = input("What's the name of the task? ")
            task_description = input("What's the task about? ")
            while not task_description.strip(): # validate that it's not just empty or spaces
                print("The description can't just be empty or spaces")
                task_description = input("What's the task about? ")
            if not self.tasks:
                next_key = "1"
            else:
                next_key = str(max(map(int, self.tasks.keys()), default=0) +1)
            new_task = {       
                'title': task_title,
                'description': task_description,
                'completed': False
            }
            self.tasks[next_key] = new_task
            self.save_tasks() # Persist changes immediately
            print("Task has been created and saved!")
        except IOError as e:
            print(e)

    def save_tasks(self):
        try:
            with open('tasks.json', 'w') as file:
                json.dump(self.tasks, file, indent=4)  #`indent=4` makes the JSON readable
        except IOError as e:
            print(f"Error saving tasks: {e}")

    def view_tasks(self):
        try:
            if not self.tasks:
                raise ValueError ("The file is empty!")
            self.sorted_tasks = {key: self.tasks[key] for key in sorted(self.tasks, key=lambda x: int(x))}
            for key, task in self.sorted_tasks.items():
                print(task)
        except ValueError as e:
            print(e)
            
    def delete_task(self):
        ...
    
    def reorder_tasks(self):
        reordered = {}
        for index,key in enumerate(sorted(self.tasks, key=lambda x: int(x)), start=1):
            reordered[str(index)] = self.tasks[key]
            self.tasks = reordered