#!/usr/bin/python3
"""a Python script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response"""

if __name__ == "__main__":
    import sys
    import urllib.request

    Obj = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(Obj) as response:
        print(response.headers.get('X-Request-Id'))
