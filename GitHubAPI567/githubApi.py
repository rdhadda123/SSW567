import requests
import json
import datetime

def my_brand(assignment):
    print("=*=*=*= Rishabh Dhadda =*=*=*=")
    print("=*=*=*= Course 2024F-SSW567-WS =*=*=*= ")
    print("=*=*=*=", assignment, "=*=*=*= ")
    
my_brand('Assignment 4a - Develop with Perspective of Tester')

def fetchRepos_Commits(github_id):
    if github_id == '':
        return "Repo Does not Exist."
    
    api_repo = f'https://api.github.com/users/{github_id}/repos'

    repos = []
    result = []

    try:
        repos_fetch = requests.get(url=api_repo)
        repos_fetch = json.loads(repos_fetch.text)
    except (TypeError, KeyError, IndexError):
        return "Fetching Repos Failed."
    
    for repo in repos_fetch:
        try:
            repos.append(repo['name'])
        except (TypeError, KeyError, IndexError):
            return "Repo Does not Exist."

    for r in repos:
        api_commit = f'https://api.github.com/repos/{github_id}/{r}/commits'

        try:
            commits_fetch = requests.get(url=api_commit)
            commits_fetch = json.loads(commits_fetch.text)
        except (TypeError, KeyError, IndexError):
            return "Fetching Commits Failed."
        
        result.append(f'Repo: {r} Number of Commits: {len(commits_fetch)}')

    return result

def main():
    github_id = input("What is your GitHub ID: ")
    for r in fetchRepos_Commits(github_id):
        print(r)

if __name__ == '__main__':
    main()