# Define an empty list to store the tasks
tasks = []

# Function to add a task to the list
def add_task(task):
    tasks.append(task)
    print("Task added successfully!")

# Function to view all tasks in the list
def view_tasks():
    if len(tasks) == 0:
        print("No tasks in the list.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

# Function to remove a task from the list
def remove_task(task_index):
    if task_index >= 1 and task_index <= len(tasks):
        del tasks[task_index - 1]
        print("Task removed successfully!")
    else:
        print("Invalid task index.")

# Main program loop
while True:
    print("\nSelect an option:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter the task to add: ")
        add_task(task)
    elif choice == "2":

