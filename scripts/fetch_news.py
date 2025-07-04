import requests

def get_it_news():
    try:
        res = requests.get("https://techcrunch.com/wp-json/wp/v2/posts?per_page=1")
        res.raise_for_status()
        post = res.json()[0]
        title = post["title"]["rendered"]
        link = post["link"]
        return f"📰 [{title}]({link})"
    except Exception as e:
        return f"⚠️ Unable to fetch news: {e}"

def update_readme():
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    news = get_it_news()
    start = "<!--START_SECTION:news-->"
    end = "<!--END_SECTION:news-->"
    new_section = f"{start}\n{news}\n{end}"
    updated = content.split(start)[0] + new_section + content.split(end)[1]

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(updated)

if __name__ == "__main__":
    update_readme()