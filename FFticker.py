#! python3
import praw
import pandas as pd
import datetime as dt

reddit = praw.Reddit(client_id='hnThiu1rW9ImKg',
                     client_secret='fa3sE8NCn-carrYqsTDpSJkU68Q',
                     redirect_uri='http://localhost:8080',
                     user_agent='testscript by /u/fakebot3')
subreddit = reddit.subreddit('FantasyFootball')
top_subreddit = subreddit.hot()
for submission in subreddit.hot(limit=20):
    print(submission.title, submission.url)
