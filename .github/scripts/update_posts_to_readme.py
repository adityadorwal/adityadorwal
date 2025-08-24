import re
import sys
import feedparser
from pathlib import Path

FEED = "https://dev.to/feed/adityadorwal"
README = Path("README.md")
START = "<!-- BLOG-POST-LIST:START -->"
END = "<!-- BLOG-POST-LIST:END -->"

def build_posts_md():
    d = feedparser.parse(FEED)
    if not d.entries:
        return "- *(no posts yet — check back soon!)*"
    lines = []
    for e in d.entries[:5]:
        title = getattr(e, "title", "Untitled").strip()
        link = getattr(e, "link", "").strip()
        lines.append(f"- [{title}]({link})")
    return "\n".join(lines)

def main():
    if not README.exists():
        print("README.md not found", file=sys.stderr)
        sys.exit(1)

    content = README.read_text(encoding="utf-8")

    if START not in content or END not in content:
        print("Markers not found in README.md", file=sys.stderr)
        sys.exit(1)

    posts_md = build_posts_md()

    pattern = re.compile(rf"({re.escape(START)})(.*?)({re.escape(END)})", re.DOTALL)
    new_content = pattern.sub(rf"\1\n{posts_md}\n\3", content)

    if new_content != content:
        README.write_text(new_content, encoding="utf-8")
        print("README.md updated")
    else:
        print("No changes to README.md")

if __name__ == "__main__":
    main()
