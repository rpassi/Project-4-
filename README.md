# Project-4:
This is a repository for project 4
## bot40cs: Who is it opposing/supporting?

My bot is posting information about former Presdient Trump and current President Biden. My score on this project should be around 28-30 points that may vary due to the amount of valid comments. I completed the six tasks in the `bot.py` file and this repo is worth 3 points. Getting more valid comments is worth up to 10 points and has been varying. 


## Extra Tasks I completed:

I made my bot create new submission posts instead of just new comments. The bot scans top level comments in the r/liberal subreddit ans posts it to the cs40_fall2022 subreddit.
This is on a new python file, `bot_submissions.py` (2 points)

The bot replies to the most highly upvoted comment in a thread that it hasn't already replied to. (2 points)

I also created a `bot_vote.py` file that loops over submissions in the class subreddit and downvotes any submission that mentions Trump and upvotes any comment that mentions Biden. There is a picture of an example below. (2 points)


<img width="1069" alt="Screen Shot 2022-11-27 at 12 05 09 PM" src="https://user-images.githubusercontent.com/112538914/204158062-c292e98e-7bbc-4f71-a869-d9165397e271.png">


The TextBlob sentiment analysis library reads comments with Trump as a negative sentiment and downvotes the comment. The TextBlob sentiment analysis library reads comments with Biden as positive and upvotes the comment. (an additional 2 points)

I used the Markovify library to create another algorithim to generate the text of comments. This algorithim is in the `bot.py` file. 

Extra credit:
1. (2 points)
3. (2 points)
4. (4 points)

Markovify-- 5 points 

There should be around 13 points of extra credit that I completed for this project.


