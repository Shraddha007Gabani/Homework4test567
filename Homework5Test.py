import unittest
import json
from Homework5 import get_repositories
from unittest import mock

def g_link(url):
    """ Fetch URL """
    if url == 'https://api.github.com/users/richkempinski/repos':
        return fetch('repos.json')

def fetch(root):
    """ Open path file """
    data = text()
    with open(root, 'r') as f:
        data.text = json.loads(f)
    return data.text

class text:
    """ Declare text class for path file """
    text = ""


class TestGithub(unittest.TestCase):
    """ Test cases """

    @mock.patch('requests.get')
    def test_get_repositories(self, mockedReq):
        """ Test case to check the user's repositories and commits"""
        mockedReq.side_effect = g_link

        repos = get_repositories('richkempinski')
        self.assertEqual(repos, "Failed to fetch the repos")


if __name__ == "__main__":
    """ Run test cases on startup """
    unittest.main(exit=False, verbosity=2)
