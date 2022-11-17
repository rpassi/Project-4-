import random
import praw

reddit = praw.Reddit('bot', user_agent='cs40')
for i in range(200):

    list_of_submissions = list(reddit.subreddit("liberal").hot(limit=None))
    submission=random.choice(list_of_submissions)
    title=submission.title
    selftext=submission.selftext

    if selftext=='':
        url=submission.url
        subreddit= reddit.subreddit("cs40_2022fall")
        subreddit.submit(title, url=url)
    else:
        subreddit= reddit.subreddit("cs40_2022fall")
        subreddit.submit(title, selftext=selftext)
    print('Created a submission')






