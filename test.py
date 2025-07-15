# Creating a Python Todo App with Memory Save Functionality
# Overview

# In this tutorial, we will create a simple command-line Todo app using Python that allows users to add, remove, and mark tasks as completed, with the added feature of saving the tasks to memory.

# Requirements
# Python 3.x (any version)
# Basic understanding of Python syntax and data structures
# App Functionality
# Add Task: Users can add new tasks to the Todo list.
# Remove Task: Users can remove tasks from the Todo list.
# Mark Task as Completed: Users can mark tasks as completed.
# Save to Memory: The Todo list is saved to memory when the app is closed, and retrieved when the app is reopened.
# Implementation

# Step 1: Create the Todo List

# We will create a Python list to store the Todo tasks. Each task will be a dictionary containing the task description, completion status, and a unique ID.

import os
todo_list = []

# Step 2: Define the Functions

# We will define four functions: add_task, remove_task, mark_task_as_completed, and save_to_memory.

# add_task
def add_task(description):
    task_id = len(todo_list) + 1
    todo_list.append({"id": task_id, "description": description, "completed": False})
    print(f"Task '{description}' added with ID {task_id}")
# remove_task
def remove_task(task_id):
    for task in todo_list:
        if task["id"] == task_id:
            todo_list.remove(task)
            print(f"Task with ID {task_id} removed")
            return
    print(f"Task with ID {task_id} not found")
# mark_task_as_completed
def mark_task_as_completed(task_id):
    for task in todo_list:
        if task["id"] == task_id:
            task["completed"] = True
            print(f"Task with ID {task_id} marked as completed")
            return
    print(f"Task with ID {task_id} not found")
# save_to_memory
import pickle

def save_to_memory():
    with open("todo_list.pkl", "wb") as f:
        pickle.dump(todo_list, f)
    print("Todo list saved to memory")

# Step 3: Create the Main App Loop

# We will create an infinite loop that prompts the user to add, remove, or mark tasks as completed. When the user quits the app, the save_to_memory function will be called.

while True:
    print("Todo App")
    print("========")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Mark Task as Completed")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        description = input("Enter task description: ")
        add_task(description)
    elif choice == "2":
        task_id = int(input("Enter task ID to remove: "))
        remove_task(task_id)
    elif choice == "3":
        task_id = int(input("Enter task ID to mark as completed: "))
        mark_task_as_completed(task_id)
    elif choice == "4":
        save_to_memory()
        break
    else:
        print("Invalid choice. Please try again.")

# Step 4: Load Saved Data

# When the app starts, we will load the saved Todo list from memory using the pickle module.

if os.path.exists("todo_list.pkl"):
    with open("todo_list.pkl", "rb") as f:
        todo_list = pickle.load(f)
    print("Todo list loaded from memory")

# Run the App

# Save the code in a file named todo_app.py and run it using Python: python todo_app.py.

# Test the App

# Add a few tasks using the app.
# Quit the app and reopen it.
# Verify that the tasks are still present and can be added to, removed, or marked as completed.

# Congratulations! You have created a simple Python Todo app with memory save functionality.

# Next Steps
# Implement user authentication and authorization
# Add more features, such as due dates, priorities, and task categorization
# Create a GUI using a library like Tkinter or PyQt
# Deploy the app to a cloud platform like Heroku or AWS