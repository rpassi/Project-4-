# Project-4:
This is a repository for project 4
## bot40cs: Who is it opposing/supporting?

My bot is posting information about former Presdient Trump and current President Biden. My score on this project should be around 28-32 points that may vary due to the amount of valid comments. I completed the six tasks in the `bot.py` file and this repo is worth 3 points. Getting more valid comments is worth up to 10 points and has been varying. I have gotten it to reach around 700 valid comments.


## Extra Tasks I completed:

I made my bot create new submission posts instead of just new comments. The bot scans top level comments in the r/liberal subreddit ans posts it to the cs40_fall2022 subreddit.
This is on a new python file, `bot_submissions.py` (2 points)

The bot replies to the most highly upvoted comment in a thread that it hasn't already replied to. (2 points)

I also created a `bot_vote.py` file that loops over submissions in the class subreddit and downvotes any submission that mentions Trump and upvotes any comment that mentions Biden. It is interesting to see that even comments that are speaking negatively about Biden are upvoted due to the TextBlob sentiment. [Here](https://old.reddit.com/r/cs40_2022fall/comments/z6a9y1/biden_deserves_props_for_his_masterful_ukraine/) is a picture of the thread below. (2 points)

<img width="1057" alt="Screen Shot 2022-11-27 at 3 46 52 PM" src="https://user-images.githubusercontent.com/112538914/204166285-e5359ce7-774a-4db7-9ded-528a2829d292.png">

I enjoyed this thread since it shows how the same sentence can be very different with replacing different keys in the dictionary calling Biden "Sleepy Joe" versus "The President". 

The TextBlob sentiment analysis library reads comments with Trump as a negative sentiment and downvotes the comment. The TextBlob sentiment analysis library reads comments with Biden as positive and upvotes the comment. This is all included in the `bot_vote.py` file (an additional 2 points).

I used the Markovify library to create another algorithim to generate the text of comments. This algorithim is in the `bot.py` file. 

Extra credit:
1. (2 points)
3. (2 points)
4. (4 points)

Markovify-- 5 points 

There should be around 13 points of extra credit that I completed for this project.

The output of the `bot_counter.py` file 
```
len(comments)= 1000
len(top_level_comments)= 142
len(replies)= 954
len(valid_top_level_comments)= 121
len(not_self_replies)= 874
len(valid_replies)= 642
========================================
valid_comments= 763
========================================
```

