<p align="center">
  <img src="assets/animated-banner.gif" alt="Aditya Dorwal — Animated Banner" />
</p>

<h1 align="center">Hi, I'm <strong>Aditya Dorwal</strong> 👋</h1>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?size=22&duration=2800&pause=700&center=true&vCenter=true&width=760&lines=AI+Engineer+who+ships+fast%2C+clean+ML+projects;Real-time+Speech+%E2%80%A2+Explainable+CV+%E2%80%A2+NLP;Open-source+mindset+%7C+DSA+daily" />
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/adityadorwal"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" /></a>
  <a href="https://adityadorwal.github.io/portfolio/"><img src="https://img.shields.io/badge/Portfolio-111?style=for-the-badge&logo=firefox-browser&logoColor=white" /></a>
  <a href="mailto:dorwaladitya18@gmail.com"><img src="https://img.shields.io/badge/Email-EE4B2B?style=for-the-badge&logo=gmail&logoColor=white" /></a>
  <img src="https://komarev.com/ghpvc/?username=adityadorwal&style=for-the-badge&color=blueviolet" />
</p>

---

## 🔥 About
I turn research ideas into **usable, fast demos**. Recently exploring **real‑time speech transcription**, **explainable computer vision**, and **efficient ML pipelines**.

- 🎓 B.Tech (AIML), KCC — 3rd year
- 🧠 Interested in: **Whisper.cpp**, **Grad‑CAM**, **local LLMs**, and **offline‑first AI tools**
- 🤝 Open to: **SDE/ML internships**, open‑source collabs
- ⚡ Real-time speech & local AI tools
- 🔍 Explainable CV with sleek UX
- 🧪 Rapid prototyping → polished demos
- ☕ Coffee → Code → Ship → Repeat


---

## 🚀 Featured Projects
### 1. Plant Disease Detection

<img src="assets/proj1.png" width="720" />

ResNet18 • Grad-CAM • Streamlit

---

### 2. Whisper.cpp Transcriber (RT)

<img src="assets/proj2.png" width="720" />

VAD • Hotword • Async

---

### 3. Dorwal AI — Assistant

<img src="assets/proj3.png" width="720" />

Local LLM • NLP • Desktop

---

### 4. LeetCode DSA Solutions

<img src="assets/proj4.png" width="720" />

Organized Java Solutions

---

### 5. MPIN Strength Checker

<img src="assets/proj5.png" width="720" />

Security heuristics (Python)

---


## 📊 Live Stats
<p align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com?user=adityadorwal&theme=dark&hide_border=true" />
</p>
<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=adityadorwal&show_icons=true&theme=transparent" />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=adityadorwal&layout=compact&theme=transparent" />
</p>

---

## 📝 Recent Posts
name: 'Update Blog Posts'

on:
  schedule:
    # Runs every 4 hours to check for new posts
    - cron: '0 */4 * * *'
  workflow_dispatch:

jobs:
  update-posts:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: gautamkrishnar/blog-post-workflow@v1
        with:
          # Your dev.to RSS feed URL
          feed_list: "https://dev.to/feed/adityadorwal"
          max_post_count: 5
          readme_file: "README.md"
          commit_message: "chore: update recent blog posts"
          comment_tag_name: "BLOG-POST-LIST"

---

## 📫 Contact
LinkedIn · Portfolio · Email

---

<p align="center">Made with ❤️ — Smooth, lightweight animations • Dark & Light variants included</p>
