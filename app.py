"""
GitHub Profile README Generator — Streamlit App
Enter any GitHub username → get a beautiful profile README
"""
import streamlit as st
from github_api import fetch_user, fetch_languages, fetch_top_repos
from generator import generate_readme, THEMES

st.set_page_config(
    page_title="GitHub Profile README Generator",
    page_icon="📝",
    layout="centered",
)

st.title("📝 GitHub Profile README Generator")
st.markdown("""
Enter any GitHub username and get a **beautiful profile README** with stats,
top languages, featured projects, and badges — ready to paste into your profile.
""")

col1, col2 = st.columns([2, 1])

with col1:
    username = st.text_input("GitHub Username", placeholder="e.g., basitali08")

with col2:
    theme = st.selectbox("Theme", list(THEMES.keys()))

if st.button("Generate README ✨", type="primary"):
    if not username.strip():
        st.error("Please enter a GitHub username")
        st.stop()

    with st.spinner(f"Fetching data for @{username}..."):
        user_data = fetch_user(username.strip())

    if user_data is None:
        st.error(f"User @{username} not found on GitHub")
        st.stop()

    with st.spinner("Fetching repositories..."):
        top_langs, total = fetch_languages(username.strip())
        top_repos = fetch_top_repos(username.strip())

    readme = generate_readme(
        username.strip(), user_data, top_langs, top_repos, theme
    )

    st.success(f"✅ README generated for @{username}!")

    st.subheader("📋 Your Profile README")
    st.code(readme, language="markdown")

    st.subheader("👀 Preview")
    st.markdown(readme)

    st.download_button(
        label="📥 Download README.md",
        data=readme,
        file_name="README.md",
        mime="text/markdown",
    )

    st.info("""
    **How to use:**
    1. Click "Download README.md"
    2. Go to github.com → Create new repo named **`your-username`**
    3. Upload this README.md → Done!
    """)

else:
    st.info("Enter a GitHub username and click Generate to see your profile README")

st.divider()
st.caption("Built with ❤️ by [Basit Ali](https://github.com/basitali08) | "
           "Data from GitHub API")
