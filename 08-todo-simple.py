def display_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Edit Task")
    print("4. Delete Task")
    print("5. Exit")
    print("------------------------")

def view_tasks(tasks):
  # View Logic
    if not tasks:
      print("Your to-do list is empty!")
    else:
      print("\nYour To-Do List:") 
      for i, task in enumerate(tasks,1):
        print(f"{i}. {task}")

def add_task(tasks):
  task = input("Enter the task to add: ")
  tasks.append(task)
  print(f"Task {task} added successfully :)")

def edit_task(tasks):
  view_tasks(tasks) 
  if tasks:
    try:
      task_number = int(input("Enter the task number to edit: ")) - 1
      if task_number >= 0 and task_number < len(tasks):
        updated_task = input("Enter the updated task: ") 
        tasks[task_number] = updated_task 
        print("Task updated successfully!")
      else:
        print("Invalid task number!")
    except ValueError:
      print("Please enter a valid number!")

def delete_task(tasks):
  view_tasks(tasks)
  if tasks:
    try:
      task_no = int(input("Enter task number to delete: ")) - 1
      if 0 <= task_no < len(tasks):
        removed_task = tasks.pop(task_no)
        print(f"Task '{removed_task}' deleted successfully")

    except ValueError:
      print("Please enter a valid number")  

def main():
  # print(__name__)
  tasks = [] 

  while True:
    display_menu()
    choice = input("Enter your choice(1-5): ")
    if choice == "1":
      view_tasks(tasks)
    elif choice =="2":
      add_task(tasks) 
    elif choice =="3":
      edit_task(tasks) 
    elif choice =="4":
      delete_task(tasks) 
    elif choice =="5":
      print("Exiting Todo-App.  Goodbye!")
      break 
    else:
      print("Invalid choice! Please try again")
      


if __name__ == "__main__":
  main() 
