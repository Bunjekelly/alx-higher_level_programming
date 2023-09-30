#!/usr/bin/python3
"""
This script send a post request with am email value supplied as cmd linearg
to script to a url supplied to the command line
"""
if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}

    obj = requests.post(url, data=data)
    print(obj.text)
