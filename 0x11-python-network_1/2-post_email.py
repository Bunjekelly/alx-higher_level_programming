#!/usr/bin/python3
"""script that takes in a URL and an email, sends a POST request to
the passed URL with the email as a parameter, and displays the body
of the response (decoded in utf-8)"""

if __name__ == "__main__":

    import urllib.request
    import urllib.parse
    import sys

    url = sys.argv[1]
    email = sys.argv[2]
    value = {'email': email}
    data = urllib.parse.urlencode(value).encode("ascii")

    obj = urllib.request.Request(url, data)
    with urllib.request.urlopen(obj) as response:
        print(response.read().decode('utf-8'))
