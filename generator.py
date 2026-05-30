"""
Generate beautiful GitHub profile README.
"""

THEMES = {
    'Default': {
        'bg': '#f0f2f5', 'text': '#1f2328', 'accent': '#0969da',
        'card_bg': '#ffffff', 'border': '#d0d7de',
    },
    'Dark': {
        'bg': '#0d1117', 'text': '#c9d1d9', 'accent': '#58a6ff',
        'card_bg': '#161b22', 'border': '#30363d',
    },
    'Cyberpunk': {
        'bg': '#0a0a0a', 'text': '#00ff41', 'accent': '#ff00ff',
        'card_bg': '#1a1a2e', 'border': '#00ff41',
    },
    'Ocean': {
        'bg': '#0f172a', 'text': '#e2e8f0', 'accent': '#38bdf8',
        'card_bg': '#1e293b', 'border': '#334155',
    },
}


def generate_readme(username, user_data, top_langs, top_repos, theme_name='Default'):
    name = user_data.get('name', username)
    bio = user_data.get('bio', 'Developer')
    location = user_data.get('location', '')
    avatar = user_data.get('avatar_url', '')
    blog = user_data.get('blog', '')
    company = user_data.get('company', '')
    followers = user_data.get('followers', 0)
    following = user_data.get('following', 0)
    public_repos = user_data.get('public_repos', 0)

    repo_lines = ''
    for repo in top_repos[:5]:
        desc = repo.get('description', '') or ''
        if len(desc) > 60:
            desc = desc[:57] + '...'
        stars = repo.get('stargazers_count', 0)
        lang = repo.get('language') or ''
        repo_lines += f"- [{repo['name']}]({repo['html_url']}) — {desc} ⭐{stars} {f'🔵{lang}' if lang else ''}\n"

    lang_badges = ''
    for lang, count in top_langs[:6]:
        lang_badges += f"![{lang}](https://img.shields.io/badge/-{lang}-blue?style=flat)"

    readme = f"""# 👋 Hi, I'm {name}

**{bio}**  
{('📍 ' + location) if location else ''} {('🏢 ' + company) if company else ''}

---

## 📊 GitHub Stats

| Stats | Top Languages |
|-------|--------------|
| ![{username}'s stats](https://github-readme-stats.vercel.app/api?username={username}&show_icons=true&theme=default&hide_border=true) | ![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username={username}&layout=compact&theme=default&hide_border=true) |

[![GitHub Streak](https://github-readme-streak-stats.herokuapp.com/?user={username}&theme=default&hide_border=true)](https://git.io/streak-stats)

---

## 🚀 Featured Projects

{repo_lines}

---

## 🛠️ Tech Stack

{lang_badges}

---

## 📫 Let's Connect

[![GitHub](https://img.shields.io/badge/GitHub-{username}-181717?logo=github)](https://github.com/{username})
{('[![LinkedIn](https://img.shields.io/badge/-LinkedIn-0077B5?logo=linkedin)](https://linkedin.com/in/' + username + ')') if username else ''}
{('[![Email](https://img.shields.io/badge/Email-{}-red?logo=gmail)](mailto:{})'.format(blog, blog) if blog and '@' in blog else '')}

---

*Profile generated with [Profile README Generator](https://github.com/basitali08/profile-readme-generator)*
"""
    return readme
