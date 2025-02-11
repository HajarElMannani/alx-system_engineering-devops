#!/usr/bin/python3
'''extend Python script to export data in the JSON format.'''
import json
import requests
from sys import argv

if __name__ == "__main__":
    req_name = requests.get("https://jsonplaceholder.typicode.com"
                            "/users")
    employees = req_name.json()
    data = {}
    for employee in employees:
        user_id = employee['id']
        req_todos = requests.get("https://jsonplaceholder.typicode.com/"
                                 "todos", params={"userId": user_id})
        todos = req_todos.json()
        values = []
        for task in todos:
            task_dict = {"username": employee["username"],
                         "task": task["title"],
                         "completed": task["completed"]}
            values.append(task_dict)
        data[user_id] = values
    with open("todo_all_employees.json", "w") as my_file:
        json.dump(data, my_file)
