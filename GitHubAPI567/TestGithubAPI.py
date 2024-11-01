import unittest
from unittest.mock import patch
from githubApi import fetchRepos_Commits
import json

class MockResponse:
    def __init__(self, json_data):
        self.json_data = json_data
        self.text = json.dumps(json_data)  # Add .text as JSON string
    
    def json(self):
        return self.json_data

class TestGithubAPI(unittest.TestCase):

    @patch('githubApi.requests.get')
    def test_invalid_user(self, mock_get):
        # Simulate an invalid user by having an empty JSON response or a 404 status
        mock_get.return_value = MockResponse('Repo Does not Exist.')
        
        github_id = 'wifhiuwebvjc'
        self.assertEqual(fetchRepos_Commits(github_id), 'Repo Does not Exist.')

    @patch('githubApi.requests.get')
    def test_empty_user_id(self, mock_get):
        # Mock response for empty GitHub ID
        mock_get.return_value = MockResponse([])
        
        github_id = ''
        self.assertEqual(fetchRepos_Commits(github_id), 'Repo Does not Exist.')

    @patch('githubApi.requests.get')
    def test_repo_length_success(self, mock_get):
        # Mock response with exactly 10 repositories
        mock_get.return_value = MockResponse([{'name': f'Repo{i}'} for i in range(10)])
        
        github_id = 'rdhadda123'
        self.assertEqual(len(fetchRepos_Commits(github_id)), 10)

    @patch('githubApi.requests.get')
    def test_repo_length_fail(self, mock_get):
        # Mock response with 10 repositories, should not match length 20
        mock_get.return_value = MockResponse([{'name': f'Repo{i}'} for i in range(10)])
        
        github_id = 'rdhadda123'
        self.assertNotEqual(len(fetchRepos_Commits(github_id)), 20)

    @patch('githubApi.requests.get')
    def test_commits_first_repo(self, mock_get):
        # Mock response to return 1 repo and then 1 commit
        def side_effect(url):
            if 'repos' in url:
                return MockResponse([{'name': 'AbstractFactoryDesignPattern'}])
            elif 'commits' in url:
                return MockResponse([{}])  # Mock 1 commit
            return MockResponse([])

        mock_get.side_effect = side_effect
        github_id = 'rdhadda123'
        self.assertEqual(fetchRepos_Commits(github_id)[0], 'Repo: AbstractFactoryDesignPattern Number of Commits: 1')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
