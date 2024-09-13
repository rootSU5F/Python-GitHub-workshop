"""
in this program we are going to create TO DO LIST app

"""
from traceback import print_tb

current_tasks = []
done_tasks = []
print("TODO LIST ACTIONS\n"
      "--------------------------------------\n"
      "1 - for add a new task\n"
      "2 - to make a specific task done\n"
      "3 - to delete a task\n"
      "4 - show all tasks\n"
      "5 - show done tasks\n"
      "6 - Exit\n"
      "--------------------------------------"

      )
def add_task(task):
    current_tasks.append(str(task))
    print("the task is added successfully !!! ")

def check_the_task(index):
    done_tasks_size = len(done_tasks)
    current_tasks_size = len(current_tasks)
    done_task = current_tasks.pop(index)
    done_tasks.append(done_task)
    if (len(done_task) > done_tasks_size and len(current_tasks) < current_tasks_size):
        print("this task is done now ! ")
    else:
        print("there is an error ocuurs !! ")

def delete_task(index):
    current_tasks.pop(index)
    print("Deleted !!")

def print_current_list():
    for task in current_tasks:
        print(task + " in progress" "\n")
def print_done_list():
    for task in done_tasks:
        print(task + " Done ! " "\n")


user_input = -1
while (True):
    print("TODO LIST ACTIONS\n"
          "--------------------------------------\n"
          "1 - for add a new task\n"
          "2 - to make a specific task done\n"
          "3 - to delete a task\n"
          "4 - show all tasks\n"
          "5 - show done tasks\n"
          "6 - Exit\n"
          "--------------------------------------"

          )
    user_input = int(input("Enter your response please depend upon the list above : "))
    if (user_input == 1 ):
        user_task = input("enter your task  : \n")
        add_task(user_task)
    elif(user_input == 2):
        print(current_tasks)
        user_task_req = int(input("which one u want to check : "))
        check_the_task((user_task_req-1))
    elif(user_input == 3 ):
        print(current_tasks)
        user_task_req = int(input("which one u want to delete : "))
        delete_task(user_task_req-1)
    elif (user_input == 4):
        print("here is the current tasks : \n")
        print_current_list()
    elif (user_input == 5):
        print("here is the done tasks : \n")
        print_done_list()
    elif user_input == 6 :
        exit()
    else :
        print("wrong entered number ")








