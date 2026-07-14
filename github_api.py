import requests

BASE_URL = "https://api.github.com/users"

def get_user_profile(username):
    url = f"{BASE_URL}/{username}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    return None


def get_repositories(username):
    url = f"{BASE_URL}/{username}/repos"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    return []