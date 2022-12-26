import re
import os

import requests

# Set the personal access token for the GitHub API
personal_access_token = os.environ["PERSONAL_ACCESS_TOKEN"]

# Set the headers for the GitHub API request
headers = {
    "Authorization": f"Token {personal_access_token}"
}

# Get the latest tag from the repository
response = requests.get(
    "https://api.github.com/repos/bin2ai/pycurtain/tags", headers=headers)
latest_tag = response.json()[0]["name"]

# Read the setup.py file
with open("setup.py", "r") as f:
    setup_py = f.read()

# Update the version in the setup.py file
setup_py = re.sub(r"version='[^']*'", f"version='{latest_tag}'", setup_py)

# Write the updated setup.py file
with open("setup.py", "w") as f:
    f.write(setup_py)
