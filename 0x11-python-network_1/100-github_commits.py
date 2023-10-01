#!/usr/bin/python3
"""a Python script that takes 2 arguments in order to
list 10 most recent commits for a github user"""

if __name__ == "__main__":
    import requests
    import sys

    repo = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    response = requests.get(url)
    try:
        commits = response.json()
        for i in range(10):
            print("{}: {}".format(commits[i]['sha'],
                                  commits[i]['commit']['author']['name']))
    except IndexError:
        pass
