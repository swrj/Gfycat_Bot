import praw
import time
import sqlite3
import config
from prawcore.exceptions import PrawcoreException

reddit = None
conn = None
c = None
flair_list = None
chosen_flair = ''
link_flair_choices = str()
submissions_commented_on = set()
submissions_to_ignore = set()

SUBREDDIT = 'fmgtestsub'
SUBMISSION_LIMIT = 1
POST_TIME_LIMIT = 90
COMMENT_FOOTNOTE = '\n\n---\n\n Bot made by John_Yuki and Swaraj.'
NEW_POST_COMMENT = 'Please flair your post:\n\n'
HELP_POST_COMMENT = 'Removed for help flair'
POST_TIME_LIMIT_COMMENT = 'Didn\'t flair post in time.'


def connect_to_reddit():
    global reddit
    global link_flair_choices
    reddit = praw.Reddit(
    client_id=config.client_id,
    client_secret=config.client_secret,
    user_agent=config.user_agent,
    username=config.username,
    password=config.password)
    for template in reddit.subreddit(SUBREDDIT).flair.link_templates:
        link_flair_choices += '* '+str(template['text'])+'\n\n'
    
def connect_to_database():
    global conn
    global c
    conn = sqlite3.connect('id_list.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS Submissions_Commented_On(Submission_ID)')
    conn.commit()
    c.execute('CREATE TABLE IF NOT EXISTS Submissions_To_Ignore(Submission_ID)')
    conn.commit()

def load_submissions():
    global submissions_commented_on
    global submissions_to_ignore
    global c
    c.execute('SELECT Submission_ID FROM Submissions_Commented_On')
    submissions_commented_on = set()
    for row in c.fetchall():
        submissions_commented_on.add(row[0])
    c.execute('SELECT Submission_ID FROM Submissions_To_Ignore')
    submissions_to_ignore = set()
    for row in c.fetchall():
        submissions_to_ignore.add(row[0])

def get_flair_list():
    global reddit
    global flair_list
    global SUBREDDIT
    flair_template = reddit.subreddit(SUBREDDIT).flair.link_templates
    flair_list = [flair['text'] for flair in flair_template]

def add_submission_to_ignore_list():
    print('add_submission_to_ignore_list()')
    global conn
    global c
    c.execute('INSERT INTO Submissions_To_Ignore VALUES(?)',(submission.id,))
    conn.commit()

def add_to_submissions_commented_on():
    print('add_submissions_to_commented_on()')
    global conn
    global c
    c.execute('INSERT INTO Submissions_Commented_On VALUES (?)', (submission.id,))
    conn.commit()
    
def remove_help_post():
    print('remove_help_post()')
    global HELP_POST_COMMENT
    global COMMENT_FOOTNOTE
    submission.reply(str(HELP_POST_COMMENT)+str(COMMENT_FOOTNOTE)).mod.distinguish()
    submission.mod.remove()
    print('Removed a help post.')

def remove_bot_comments():
    print('remove_bot_comments()')
    for comment in submission.comments:
        try:
            if comment.author.name == reddit.user.me():
                comment.delete()
        except:
            pass

def remove_old_post():
    print('remove_old_post()')
    global COMMENT_FOOTNOTE
    global POST_TIME_LIMIT_COMMENT
    remove_bot_comments()
    submission.reply(str(POST_TIME_LIMIT_COMMENT)+str(COMMENT_FOOTNOTE)).mod.distinguish()
    submission.mod.remove()
    print('Removed an old post.')


def check_comments():
    print('check_comments()')
    global flair_list
    global chosen_flair
    all_comments = submission.comments.list()
    for comment in all_comments:
        comment_parent = comment.parent()
        if 'SETFLAIR' in comment.body.upper() and comment.author == submission.author and comment_parent.author == reddit.user.me():
            index = comment.body.find('SETFLAIR')
            for flair in flair_list:
                if flair.upper() in comment.body.upper():
                    chosen_flair = flair.upper()
            if chosen_flair in flair_list:
                if chosen_flair == 'HELP':
                    remove_bot_comments()
                    remove_help_post()
                    add_submission_to_ignore_list()
                elif chosen_flair != 'HELP' and chosen_flair.upper() in flair_list:
                    set_flair()
                    remove_bot_comments()

def set_flair():
    print('set_flair()')
    global chosen_flair
    submission.mod.flair(text=chosen_flair.upper())
    add_submission_to_ignore_list()
    print('Set flair.')

def check_flair():
    print('check_flair()')
    global flair_list
    if submission.link_flair_text == 'HELP':
        remove_help_post()
    elif submission.link_flair_text in flair_list:
        remove_bot_comments()
        add_submission_to_ignore_list()

def send_flair_reminder():
    global NEW_POST_COMMENT
    add_to_submissions_commented_on()
    submission.reply(str(NEW_POST_COMMENT)+str(link_flair_choices)+str(COMMENT_FOOTNOTE)).mod.distinguish()
    print('Sent flair reminder.')

if __name__ == '__main__':
    connect_to_reddit()
    print('Logged in as:', reddit.user.me())
    connect_to_database()
    print('Connected to local database.')
    get_flair_list()
    print('Found subreddit link flairs.')
    while True:
        for submission in reddit.subreddit(SUBREDDIT).new(limit=SUBMISSION_LIMIT):
            load_submissions()
            if submission.id in submissions_commented_on and submission.id not in submissions_to_ignore:
                if submission.link_flair_text == None:
                    check_comments()
                    check_flair()
                elif time.time() - submission.created_utc > POST_TIME_LIMIT:
                    remove_old_post()
            elif submission.id not in submissions_commented_on and submission.id not in submissions_to_ignore:
                send_flair_reminder()
