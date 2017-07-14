import praw
import config
import time

def bot_login():
    print("Logging in....")
    reddit_instance=praw.Reddit(client_id=config.client_id,
                client_secret=config.client_secret,
                user_agent='linux:Gfycat_Link_Fixer:v0.1 (by /u/Gfy_cat_Fixer_Bot)',
                username=config.username,
                password=config.password)
    print("Logged in.")
    return reddit_instance

def run_bot(reddit_instance):
    print("Searching for broken links")
    for submission in reddit_instance.subreddit('RocketLeague+PUBATTLEGROUNDS+Rainbow6+gaming+titanfall').new(limit=20):
        if "gfycat.com/gifs/detail/" in submission.url:
            all_comments=submission.comments.list()
            for items in all_comments: #check to prevent duplicate comments in thread
                user_name=items.comment
                if user_name.author=='Gfy_cat_Fixer_Bot':
                    print "Duplicate"
                    break
            print("Broken link found")
            unique_URL=submission.url[31:] #extracting unique gfycat identifier from bloated link
            fixed_link="https://www.gfycat.com/"+unique_URL
            print(fixed_link)
            comment="[Direct link to GIF](%s)  [^why ^am ^I ^posting ^this?]" \
                    "(https://gist.github.com/anonymous/e42ca1e302d0dcd4c4c4a949e8a5c682)"%fixed_link
            submission.reply(comment)
    time.sleep(600) #Bot rests for 10 minutes before running again

reddit_instance=bot_login()
while True:
    run_bot(reddit_instance)
