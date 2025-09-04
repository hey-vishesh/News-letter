import time
print("Welcome to the Daily Briefing!")
print(f"Date: {time.strftime('%Y-%m-%d')} and Time: {time.strftime('%H:%M:%S')}")
print("-----------------------------------")


from modules import jokes
print("--------- JOKE OF THE DAY ---------")
print(jokes.get_joke())
print("-----------------------------------")
from modules import news
print("--------- TOP NEWS HEADLINES ---------")
print(news.get_news())
print("--------------------------------------")
from modules import reddit
print("--------- TOP REDDIT POSTS ---------")
reddit.posts()
print("-----------------------------------")