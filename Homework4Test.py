import unittest
from Homework4 import get_info_repository

class TestgetRepo(unittest.TestCase):
    def test_repo(self):
        expected = ['User: Shraddha007Gabani',
'Repo: 567_Homework1 Number of commits: 5',
'Repo: helloworld Number of commits: 2',
'Repo: Homework4test567 Number of commits: 9',
'Repo: HW05_567 Number of commits: 2',
'Repo: Parse-GEDCOM Number of commits: 30',
'Repo: Student-Repository Number of commits: 6',
'Repo: Student_Repository Number of commits: 23',
'Repo: Triangle567 Number of commits: 4']

        self.assertEqual(get_info_repository('Shraddha007Gabani'), expected)

if __name__ == '__main__':
    unittest.main()
