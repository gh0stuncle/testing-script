import requests
from dotenv import load_dotenv
import os

from datetime import datetime
load_dotenv()

# Replace with your personal access token
ACCESS_TOKEN = os.getenv('GITHUB_ACCESS_TOKEN')
# Replace with the owner and repository you want to fetch commits from
OWNER = 'gh0stuncle'
REPO = 'testing-script'

def fetch_commits(owner, repo, token):
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Error fetching commits: {response.status_code}")

    commits = response.json()
    for commit in commits:
        commit_sha = commit['sha']
        commit_author = commit['commit']['author']['name']
        commit_date = commit['commit']['author']['date']
        commit_message = commit['commit']['message']
        commit_url = commit['html_url']
        print(f"Commit: {commit_sha}")
        print(f"Author: {commit_author}")
        print(f"Date: {commit_date}")
        print(f"Message: {commit_message}")
        print(f"URL: {commit_url}")
        print('-' * 80)

if __name__ == '__main__':
    fetch_commits(OWNER, REPO, ACCESS_TOKEN)
