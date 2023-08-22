#!/usr/bin/python3
'''Returns information about'''
import requests
import sys


def get_employee_todo_list(employee_id):
    user = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}").json()
    todos = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}").json()
    
    done_tasks = [task["title"] for task in todos if task["completed"]]
    total_tasks = len(todos)
    
    print(f"Employee {user['name']} is done with tasks ({len(done_tasks)}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t{task}")
        
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_list(employee_id)
