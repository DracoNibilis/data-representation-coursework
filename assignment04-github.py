# Author: Magdalena Malik

# Import modules
from github import Github
import requests

# Get Api Key
file_name = "gitHubKey.txt"

# function to get key from file
def get_file_content(file_name):
    with open(file_name, "r") as f:
        return f.read().strip()
api_key = get_file_content(file_name)
# Check if content read correctly
#print(api_key)

g = Github(api_key)

# Check if connected to repo and print repo url
repo = g.get_repo("DracoNibilis/private_one")
#print(repo.clone_url)

# Get file from repo
fileInfo = repo.get_contents("text.txt")
urlOfFile = fileInfo.download_url
response = requests.get(urlOfFile)

# Replace name "Andrew" with "Magdalena" in text file
contentOfFile = response.text
newContents = contentOfFile.replace("Andrew", "Magdalena")
print(newContents)

# Update changes into file
gitHubResponse = repo.update_file(fileInfo.path, "MM", newContents, fileInfo.sha)

#print(gitHubResponse)