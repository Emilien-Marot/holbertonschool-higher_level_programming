#!/usr/bin/env python3
def fetch_and_print_posts():
    import requests as rq
    r = rq.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {r.status_code}")
    if r.status_code != 200:
        return
    data = r.json()
    for line in data:
        print(line["title"])
        


def fetch_and_save_posts():
    import requests as rq
    r = rq.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {r.status_code}")
    if r.status_code != 200:
        return
    data = r.json()
    list_dict = []
    keys = ["id", "title", "body"]
    for line in data:
        list_dict.append({k: line[k] for k in keys})
    import csv
    with open("posts.csv", "w", encoding="utf-8") as file:
        csvwriter = csv.DictWriter(file, keys)
        csvwriter.writeheader()
        csvwriter.writerows(list_dict)
