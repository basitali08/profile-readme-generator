"""
GitHub API wrapper to fetch user data.
"""
import requests


def fetch_user(username):
    url = f"https://api.github.com/users/{username}"
    r = requests.get(url)
    if r.status_code == 404:
        return None
    r.raise_for_status()
    return r.json()


def fetch_repos(username):
    url = f"https://api.github.com/users/{username}/repos?per_page=100&sort=updated"
    r = requests.get(url)
    r.raise_for_status()
    return r.json()


def fetch_languages(username):
    repos = fetch_repos(username)
    lang_count = {}
    for repo in repos:
        lang = repo.get('language')
        if lang:
            lang_count[lang] = lang_count.get(lang, 0) + 1
    total = sum(lang_count.values())
    sorted_langs = sorted(lang_count.items(), key=lambda x: -x[1])
    return sorted_langs, total


def fetch_top_repos(username):
    repos = fetch_repos(username)
    repos_with_stars = [r for r in repos if r.get('stargazers_count', 0) > 0]
    repos_with_stars.sort(key=lambda x: -x['stargazers_count'])
    return repos_with_stars[:6]
