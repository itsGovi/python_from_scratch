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
                print("No Task available to view.")
                return
            for key in sorted(self.tasks, keys=lambda x: int(x)):
                task = self.tasks[key]
                print(f"Task {key}: {task['title']} - {task['description']}")
        except ValueError as e:
            print(e)
            
    def delete_task(self):
        try:
            if not self.tasks:
                print("No tasks available to delete.")
                return
            
            print("Tasks Available: ")
            for key, task in self.tasks.items():
                print(f"Task {key}: {task['title']}")
            delete_task = input("What task do you wanna delete, please enter task no.: ")
            while not delete_task.isdigit() or delete_task not in self.tasks:
                print("Please enter a valid task number.")
                delete_task = input("What task do you want to delete? ")


            print(f"Task Details:\n Title: {self.tasks[delete_task]['title']}\n Descritption: {self.tasks[delete_task]['description']}")
            max_no_invalid_inputs = 5
            invalid_input_count = 0
            confirm_delete = input("Do you want to delete this task(y/n): ").lower()
            while confirm_delete not in ['y', 'n'] and invalid_input_count < max_no_invalid_inputs:
                confirm_delete = input("Please enter 'y' or 'n': ").lower()
                if confirm_delete not in ['y', 'n']:
                    print(f"Invalid input. Please enter 'y' or 'n'. You have {max_no_invalid_inputs} left before exit.")    
                    invalid_input_count += 1
                if invalid_input_count == max_no_invalid_inputs:
                    print("Too many invalid input errors. Exiting...")
                    return            
            if confirm_delete == 'y':
                del self.tasks[delete_task]
                if self.tasks:
                    self.reorder_tasks()
                self.save_tasks()
                print("Task deleted successfully!")
            elif confirm_delete == 'n':
                print("Deletion Cancelled.")             
        except Exception as e:
            print(f"An error occured: {e}")
    
    def reorder_tasks(self):
        if not self.tasks:
            return
        reordered = {str(index): self.tasks[key] for index, key in enumerate(sorted(self.tasks.keys(), key=lambda x: int(x)), start=1)}
        self.tasks = reordered