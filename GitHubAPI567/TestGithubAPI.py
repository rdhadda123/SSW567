import unittest
from githubApi import fetchRepos_Commits

class TestGithubAPI(unittest.TestCase):

    def test_invalid_user(self):
        # Testing with invalid GitHub ID
        github_id = 'wifhiuwebvjc'
        self.assertEqual(fetchRepos_Commits(github_id), 'Repo Does not Exist.')

    def test_empty_user_id(self):
        # Test with an empty GitHub ID
        github_id = ''
        self.assertEqual(fetchRepos_Commits(github_id), 'Repo Does not Exist.')

    def test_repo_length_success(self):
        #Testing if number of repos is fetched properly
        github_id = 'rdhadda123'
        self.assertEqual(len(fetchRepos_Commits(github_id)), 10)

    def test_repo_length_fail(self):
        #Testing if number of repos is fetched incorrectly
        github_id = 'rdhadda123'
        self.assertNotEqual(len(fetchRepos_Commits(github_id)), 20)

    def test_commits_first_repo(self):
        #Testing if message for first repo is correct 
        github_id = 'rdhadda123'
        self.assertEqual(fetchRepos_Commits(github_id)[0], 'Repo: AbstractFactoryDesignPattern Number of Commits: 3')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()