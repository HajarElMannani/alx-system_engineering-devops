#!/usr/bin/python3
'''script that returns information about his/her TODO list
 progress. usin a REST API'''
import requests
from sys import argv

if __name__ == "__main__":
    req_name = requests.get("https://jsonplaceholder.typicode.com"
                            "/users/{}/".format(argv[1]))
    employee = req_name.json()
    req_todos = requests.get("https://jsonplaceholder.typicode.com/"
                             "todos", params={"userId": argv[1]})
    todos = req_todos.json()
    username = employee['name']
    total = len(todos)
    success = []
    for task in todos:
        if task['completed'] is True:
            success.append(task['title'])
    succ_count = len(success)
    print(f"Employee {username} is done with tasks({succ_count}/{total}):")
    for i in success:
        print(f"\t {i}")
