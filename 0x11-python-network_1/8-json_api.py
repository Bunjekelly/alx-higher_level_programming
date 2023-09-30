#!/usr/bin/python3
""" a Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter."""

if __name__ == "__main__":
    import requests
    import sys

    url = "http://0.0.0.0:5000/search_user"

    if len(sys.argv) == 2:
        values = {"q": sys.argv[1]}
    else:
        values = {"q": ""}

    response = requests.post(url, data=values)
    try:
        json = response.json()
        if json == {}:
            print("No result")
        else:
            print("[{}] {}".format(json["id"], json["name"]))
    except ValueError:
        print("Not a valid JSON")
