import praw
import config
import time

def bot_login():
    print("Logging in....")
    reddit_instance = praw.Reddit(client_id=config.client_id,
                client_secret = config.client_secret,
                user_agent = 'Reddit Gfycat Link Fixer:v1.0 (by /u/Gfy_cat_Fixer_Bot)',
                username = config.username,
                password = config.password) #storing client_secret, password and client_id client side for security
    print("Logged in.")
    return reddit_instance

def run_bot(reddit_instance):
    reddit_instance.domain('gfycat.com')
    subreddit = reddit_instance.subreddit('all')
    for submission in subreddit.stream.submission(): #using subreddit.stream.submissions to avoid missing new posts
        if "gfycat.com/gifs/detail/" in submission.url:
            all_comments = submission.comments
            for items in all_comments: #check to prevent duplicate comments in thread
                user_name = items.comment
                if user_name.author is 'Gfy_cat_Fixer_Bot':
                    print "Already fixed this link. Moving on..."
                    continue
            print("Broken link found!")
            unique_URL = submission.url[31:] #extracting unique gfycat identifier from bloated link
            fixed_link = "https://www.gfycat.com/"+unique_URL
            print(fixed_link)
            comment = "[Direct link to GIF](%s)  " \
                    "  [^why ^am ^I ^posting ^this?]" \
                    "(https://gist.github.com/anonymous/e42ca1e302d0dcd4c4c4a949e8a5c682)"%fixed_link
            submission.reply(comment)

reddit_instance = bot_login()
while True:
    try:
        run_bot(reddit_instance)
    except:
        continue #restarting bot in case of exception
    time.sleep(15) #pausing script for 15 seconds to comply with Reddit's API framework
