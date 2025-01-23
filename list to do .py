import sys

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def update_task(self, index, new_task):
        if self.valid_index(index):
            self.tasks[index]["task"] = new_task

    def complete_task(self, index):
        if self.valid_index(index):
            self.tasks[index]["completed"] = True

    def delete_task(self, index):
        if self.valid_index(index):
            self.tasks.pop(index)

    def list_tasks(self):
        for i, task in enumerate(self.tasks):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{i}. {task['task']} - {status}")

    def valid_index(self, index):
        if 0 <= index < len(self.tasks):
            return True
        print("Invalid task index")
        return False

def main():
    todo_list = ToDoList()
    actions = {
        '1': lambda: todo_list.add_task(input("Enter the task: ")),
        '2': lambda: todo_list.update_task(int(input("Enter the task index to update: ")), input("Enter the new task: ")),
        '3': lambda: todo_list.complete_task(int(input("Enter the task index to complete: "))),
        '4': lambda: todo_list.delete_task(int(input("Enter the task index to delete: "))),
        '5': todo_list.list_tasks,
        '6': sys.exit
    }

    while True:
        print("\nTo-Do List Application\n1. Add Task\n2. Update Task\n3. Complete Task\n4. Delete Task\n5. List Tasks\n6. Exit")
        action = actions.get(input("Enter your choice: "), lambda: print("Invalid choice. Please try again."))
        action()

if __name__ == "__main__":
    main()
