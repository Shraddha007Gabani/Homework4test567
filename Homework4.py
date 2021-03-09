"""author: Shraddha Gabani"""

import requests
import json


def get_info_repository(usr_name):
    """get users repository"""
    o1 = []
    repos = json.loads(requests.get('https://api.github.com/users/{0}/repos'.format(usr_name)).text)
    o1.append('User: {}'.format(usr_name))

    try:
        repos[0]['name']
    except (TypeError, KeyError, IndexError):
        return 'cannot find the yuser name'

    try:
        for repo in repos:
            repo_name = repo['name']
            o1.append('Repo: {0} Number of commits: {1}'.format(repo_name, len(json.loads(requests.get('https://api.github.com/repos/{}/{}/commits'.format(usr_name, repo_name)).text))))
    except (TypeError, KeyError, IndexError):
        return 'cannot recognize that how much commit are made in repo'
    return o1


if __name__ == '__main__':
    """call main function"""
    u_name= input("enter the vaild user name")
    for i in get_info_repository(u_name):
        print(i)
