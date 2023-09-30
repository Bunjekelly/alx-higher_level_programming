#!/usr/bin/python3
"""A script that takes in a URL, sends a request to the URL and displays the
body of the response (decoded in utf-8)"""
if __name__ == "__main__":
    import sys
    import urllib.request

    url = sys.argv[1]
    Obj = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(Obj) as response:
            print(response.read().decode("utf-8"))
    except urllib.request.HTTPError as e:
        print(f"Error code: {e.code}")