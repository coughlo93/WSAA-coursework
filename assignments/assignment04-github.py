from github import Github
import requests
from config import config as cfg

# Load API key securely from config
apikey = cfg["githubkey"]
g = Github(apikey)

# Set repo and file details
repo_name = "coughlo93/WSAA-coursework"
file_path = "assignments/test.txt"
replacement_name = "Owen"  # Replace "Andrew" with your name

# Get the repository
repo = g.get_repo(repo_name)

# Get the file content
file_info = repo.get_contents(file_path)
download_url = file_info.download_url
response = requests.get(download_url)
content = response.text

# Replace "Andrew" with your name
updated_content = content.replace("Andrew", replacement_name)

# Commit and push the updated file
commit_message = "Replaced 'Andrew' with 'Owen' using script"
repo.update_file(
    file_info.path, 
    commit_message, 
    updated_content, 
    file_info.sha
)

print("✅ File updated and pushed to GitHub.")
