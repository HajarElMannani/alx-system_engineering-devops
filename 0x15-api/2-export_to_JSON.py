#!/usr/bin/python3
'''extend Python script from task 0 to export data in the JSON format'''
import json
import requests
from sys import argv

if __name__ == "__main__":
    req_name = requests.get("https://jsonplaceholder.typicode.com"
                            "/users/{}/".format(argv[1]))
    employee = req_name.json()
    req_todos = requests.get("https://jsonplaceholder.typicode.com/"
                             "todos", params={"userId": argv[1]})
    todos = req_todos.json()
    username = employee['username']
    values = []
    for task in todos:
        task_dict = {"task": task["title"],
                     "completed": task["completed"],
                     "username": username}
        values.append(task_dict)
    data = {f"{argv[1]}": values}
    with open(f"{argv[1]}.json", "w") as my_file:
        json.dump(data, my_file)
