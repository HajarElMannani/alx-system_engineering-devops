#!/usr/bin/python3
'''extend Python script from task 0 to export data in the CSV format.'''
import csv
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
    data = []
    for task in todos:
        dict_task = {"id": argv[1],
                     "username": username,
                     "completed": task["completed"],
                     "title": task["title"]}
        data.append(dict_task)
    with open(f"{argv[1]}.csv", "w", newline="") as my_file:
        fieldnames = ["id", "username", "completed", "title"]
        write = csv.DictWriter(my_file, fieldnames=fieldnames,
                               quoting=csv.QUOTE_ALL)
        write.writerows(data)
