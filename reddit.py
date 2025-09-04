import requests

def posts():
    """Legacy function for console output"""
    url = "https://www.reddit.com/r/pics/hot.json?limit=5"
    headers = {"User-agent": "Redditposts"}
    response = requests.get(url, headers=headers)
    posts = response.json()["data"]["children"]

    for post in posts:
        data = post["data"]
        title = data["title"]
        text = data["selftext"][:200]
        image = data.get("url_overridden_by_dest", None)
        thumbnail = data.get("thumbnail", None)

        print("Title:", title)
        print("Description:", text if text else "No description")
        print("Image URL:", image)
        print("Thumbnail:", thumbnail)
        print("---------------------------------")
    return 0

def get_posts_data():
    """Get Reddit posts as structured data for API"""
    try:
        url = "https://www.reddit.com/r/pics/hot.json?limit=5"
        headers = {"User-agent": "Redditposts"}
        response = requests.get(url, headers=headers)
        posts = response.json()["data"]["children"]

        formatted_posts = []
        for post in posts:
            data = post["data"]
            formatted_posts.append({
                'title': data['title'],
                'selftext': data['selftext'][:200] if data['selftext'] else '',
                'url': data.get('url_overridden_by_dest', ''),
                'thumbnail': data.get('thumbnail', ''),
                'score': data.get('score', 0),
                'num_comments': data.get('num_comments', 0)
            })
        
        return formatted_posts
    except Exception as e:
        print(f"Error fetching Reddit posts: {e}")
        return []