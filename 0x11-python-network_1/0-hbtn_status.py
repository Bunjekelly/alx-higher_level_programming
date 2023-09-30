#!/usr/bin/python3
"""a Python script that fetches https://alx-intranet.hbtn.io/status"""

if __name__ == "__main__":

    import urllib.request


    url = "https://alx-intranet.hbtn.io/status"
    obj = urllib.request.Request(url)
    with urllib.request.urlopen(obj) as response:
        content = response.read()
        print("Body response:")
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content}")
        print(f"\t- utf8 content: {content.decode('utf-8')}")