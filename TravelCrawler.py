#!/usr/bin/env python
# coding: utf-8

# In[1]:


import praw
import json
import datetime as dt


# In[2]:


reddit = praw.Reddit(client_id='Jxj7iGi2PGFtRA',
                     client_secret='JJkLXqSWpgyeavjbLKMw-tVk678',
                     user_agent='Reddit Crawler',
                     username='Mishkat076',
                     password='Mishkat076')


# In[3]:


with open('subreddits.txt', 'r') as infile:
    subreddits = infile.readlines()


# In[4]:


subreddits = [subreddit.rstrip('\n') for subreddit in subreddits]


# In[5]:


keyval = {
            'title':'title', 
            'selftext':'body'
         } # list all key:value except for comments


# In[6]:


def get_comments(submission):
    submission.comments.replace_more(limit=None)
    return [comment.body for comment in submission.comments.list()]


# In[7]:


data = []
for subreddit in subreddits:
    top = reddit.subreddit(subreddit).top(limit=1)
    for submission in top:
        values = vars(submission)
        datum = {keyval[key]:values[key] for key in keyval.keys()}
        datum['comments'] = get_comments(submission)
        data.append(datum)


# In[8]:


with open('data.json', 'w') as outfile:
    json.dump(data, outfile)


# In[ ]:




