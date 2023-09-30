#!/usr/bin/python3
"""
A script that send a request to a given url and prints the content of the
X-Request-Id response header variable
"""
if __name__ == "__main__":
    import requests
    import sys

    Obj = requests.get(sys.argv[1])
    print(Obj.headers.get("X-Request-Id"))
