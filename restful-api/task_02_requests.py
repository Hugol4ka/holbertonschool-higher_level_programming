#!/usr/bin/python3
import requests
import csv

def fetch_and_print_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    response.status_code
    print("Status Code: {}".format(response.status_code))

    if response.status_code == 200:
        data = response.json()
        for post in data:
            print(post["title"])

def fetch_and_save_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    data = response.json()

    filtered_posts = []
    for post in data:
        post_dict = {
            "id": post["id"],
            "title": post["title"],
            "body": post["body"]
        }
        filtered_posts.append(post_dict)

        with open('posts.csv', mode='w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(filtered_posts)

