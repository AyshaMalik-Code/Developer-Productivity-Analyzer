def get_total_stars(repos):
    return sum(repo["stargazers_count"] for repo in repos)

def get_languages(repos):
    languages = {}

    for repo in repos:
        lang = repo["language"]

        if lang:
            languages[lang] = languages.get(lang, 0) + 1

    return languages

def get_top_repo(repos):
    if not repos:
        return None

    return max(repos, key=lambda x: x["stargazers_count"])