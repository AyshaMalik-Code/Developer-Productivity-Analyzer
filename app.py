import streamlit as st
import pandas as pd
from github_api import get_user_profile, get_repositories
from analytics import get_total_stars, get_languages, get_top_repo

# Page Configuration
st.set_page_config(
    page_title="Developer Productivity Analyzer",
    page_icon="🚀",
    layout="wide"
)

# Title
st.title("🚀 Developer Productivity Analyzer")

# Username Input
username = st.text_input(
    "Enter GitHub Username",
    placeholder="e.g. AyshaMalik-Code"
)

if username:
    profile = get_user_profile(username)
    repos = get_repositories(username)

    if profile:

        # ---------------- PROFILE SECTION ----------------
        st.subheader("👤 Profile Information")

        col1, col2, col3 = st.columns(3)

        col1.metric("Followers", profile["followers"])
        col2.metric("Following", profile["following"])
        col3.metric("Repositories", profile["public_repos"])

        st.write(f"### Name: {profile.get('name', 'Not Available')}")
        st.write(f"### Bio: {profile.get('bio', 'No bio available')}")

        # ---------------- ANALYTICS SECTION ----------------
        total_stars = get_total_stars(repos)
        languages = get_languages(repos)
        top_repo = get_top_repo(repos)

        st.divider()
        st.subheader("📊 Productivity Insights")

        col4, col5, col6 = st.columns(3)

        col4.metric("⭐ Total Stars", total_stars)
        col5.metric("💻 Languages Used", len(languages))
        col6.metric("📁 Active Repositories", len(repos))

        # Top Repository
        if top_repo:
            st.success(
                f"🏆 Top Repository: {top_repo['name']} "
                f"({top_repo['stargazers_count']} ⭐)"
            )

        # Language Chart
        if languages:
            st.subheader("💻 Programming Languages Usage")

            df = pd.DataFrame(
                list(languages.items()),
                columns=["Language", "Repositories"]
            )

            st.bar_chart(df.set_index("Language"))

        # Repository List
        st.divider()
        st.subheader("📂 Repository Details")

        for repo in repos:
            st.write(f"### 🔹 {repo['name']}")
            st.write(
                f"⭐ Stars: {repo['stargazers_count']} | "
                f"🍴 Forks: {repo['forks_count']} | "
                f"💻 Language: {repo['language']}"
            )
            st.write(repo.get("description", "No description available"))
            st.write("---")

    else:
        st.error("❌ GitHub user not found.")