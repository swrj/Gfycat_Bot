import praw
import config
import time

def bot_login():
    print("Logging in....")
    reddit_instance=praw.Reddit(client_id=config.client_id,
                client_secret=config.client_secret,
                user_agent='linux:Gfycat_Link_Fixer:v0.1 (by /u/Gfy_cat_Fixer_Bot)',
                username=config.username,
                password=config.password) //storing sensitive information in a seperate config file
    print("Logged in.")
    return reddit_instance

def run_bot(reddit_instance):
    print("Searching for broken links")
    for submission in reddit_instance.subreddit('RocketLeague').new(limit=10):
        if "gfycat.com/gifs/detail/" in submission.url:
            print("Broken link found")
            unique_URL=submission.url[31:]
            fixed_link="https://www.gfycat.com/"+unique_URL
            print(fixed_link)
            comment="[It seems you forgot to provide the direct Gfycat URL, click here to be directed " \
                    "to the fixed link](%s)"%fixed_link
            submission.reply(comment)
    time.sleep(300)

reddit_instance=bot_login()
while True:
    run_bot(reddit_instance)
