# Project-4:
This is a repository for project 4
## bot40cs: Who is it opposing/supporting?

My bot is posting information about former Presdient Trump and current President Biden. 





## Tasks I completed:

I made my bot create new submission posts instead od just new comments. The bot scans top level comments in the r/liberal subreddit ans posts it to the cs40_fall2022 subreddit.
This is on a new python file, `bot_submissions.py`

The bot replies to the most highly upvoted comment in a thread that it hasn't already replied to. 

I also created a `bot_vote.py` file that loops over submissions in the class subreddit and downvotes any submission that mentions Trump. The TextBlob sentiment analysis library reads comments with Trump as a negative sentiment and downvotes the comment. 
