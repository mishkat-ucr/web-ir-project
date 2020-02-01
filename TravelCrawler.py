import praw
import json
import datetime as dt
counter = 0

reddit = praw.Reddit(client_id='Jxj7iGi2PGFtRA',
                     client_secret='JJkLXqSWpgyeavjbLKMw-tVk678',
                     user_agent='Reddit Crawler',
                     username='Mishkat076',
                     password='Mishkat076')

with open('subreddits.txt', 'r') as infile:
    subreddits = infile.readlines()

subreddits = [subreddit.rstrip('\n') for subreddit in subreddits]

keyval = {
            'title':'title', 
            'selftext':'body',
            'id':'id',
            'url':'image',
            'num_comments':'num_comments',
            'permalink':'link',
            'score':'upvotes'
         } # list all key:value except for comments

def get_comments(submission):
    submission.comments.replace_more(limit=None)
    return [comment.body for comment in submission.comments.list()]

data = []
for subreddit in subreddits:
    top = reddit.subreddit(subreddit).top(limit=5) #change limits here, max = 999
    print('collecting subreddit: %s'%subreddit)
    for submission in top:
        counter+=1
        print ('post: %d' %counter)
        values = vars(submission)
        datum = {keyval[key]:values[key] for key in keyval.keys()}
        datum['comments'] = get_comments(submission)
        data.append(datum)

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)






