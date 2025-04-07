from github import Github
import requests
from config import config as cfg

# Get GitHub API key from config
apikey = cfg["githubkey"]
g = Github(apikey)

# Connect to the repository
repo = g.get_repo("coughlo93/WSAA-coursework")

# Path to the file to edit
file_path = "assignments/test.txt"

# Get the file info and its contents
file_info = repo.get_contents(file_path)
url = file_info.download_url
response = requests.get(url)
content = response.text

# Replace "Andrew" with "Owen"
updated_content = content.replace("Andrew", "Owen")

# Commit the updated file
commit_message = "Replaced 'Andrew' with 'Owen' via script"
update_response = repo.update_file(
    path=file_path,
    message=commit_message,
    content=updated_content,
    sha=file_info.sha
)

# Optional print for confirmation
print("File updated:", update_response["content"].path)
print("Commit SHA:", update_response["commit"].sha)
