import json
import os

class ToDoList:
    def __init__(self):
        self.tasks = {}
        self.load_tasks()

    def load_tasks(self):
        """Load tasks from a file, handling errors gracefully."""
        try:
            if os.path.exists('tasks.json'):
                with open('tasks.json', 'r') as file:
                    self.tasks = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading tasks: {e}")
            self.tasks = {}  # Reset to empty if load fails

    def save_tasks(self):
        """Save tasks to a file."""
        try:
            with open('tasks.json', 'w') as file:
                json.dump(self.tasks, file, indent=4)
        except IOError as e:
            print(f"Error saving tasks: {e}")

    def run(self):
        """Run the to-do list application."""
        while True:
            action = input("What do you want to do? \n 1. Create new task \n 2. View Current task(s) \n 3. Delete a task \n 'quit' to exit: ").strip().lower()
            if action == '1':
                self.create_task()
            elif action == '2':
                self.view_tasks()
            elif action == '3':
                self.delete_task()
            elif action in ['quit', 'exit']:
                print("Exiting application.")
                break
            else:
                print("Invalid input, please try again.")

    def create_task(self):
        """Create and save a new task."""
        task_title = input("What's the name of the task? ").strip()
        while not task_title:
            print("The title can't be empty.")
            task_title = input("What's the name of the task? ").strip()

        task_description = input("What's the task about? ").strip()
        while not task_description:
            print("The description can't be empty.")
            task_description = input("What's the task about? ").strip()

        # Generate a new key for the task
        next_key = str(max(map(int, self.tasks.keys()), default=0) + 1)

        self.tasks[next_key] = {
            'title': task_title,
            'description': task_description,
            'completed': False
        }
        self.save_tasks()
        print("Task created successfully!")

    def view_tasks(self):
        """Display all tasks."""
        if not self.tasks:
            print("No tasks available.")
            return

        for key in sorted(self.tasks, key=int):  # Sort tasks numerically by key
            task = self.tasks[key]
            print(f"Task {key}: {task['title']} - {task['description']}")

    def delete_task(self):
        """Delete a specified task."""
        if not self.tasks:
            print("No tasks available to delete.")
            return

        print("Available tasks:")
        for key, task in self.tasks.items():
            print(f"Task {key}: {task['title']}")

        delete_task = input("Enter task number to delete: ").strip()
        while not delete_task.isdigit() or delete_task not in self.tasks:
            print("Invalid task number. Please try again.")
            delete_task = input("Enter task number to delete: ").strip()

        print(f"Task {delete_task} details:")
        print(f"Title: {self.tasks[delete_task]['title']}\nDescription: {self.tasks[delete_task]['description']}")

        confirm_delete = input("Do you want to delete this task (y/n)? ").strip().lower()
        if confirm_delete == 'y':
            del self.tasks[delete_task]
            self.save_tasks()
            print("Task deleted successfully!")
        else:
            print("Task deletion canceled.")

if __name__ == "__main__":
    todo = ToDoList()
    todo.run()