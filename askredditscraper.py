import praw
from client_codes import client_id, client_secret, user_agent

# Initialize PRAW
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent
)

# Select the subreddit
subreddit = reddit.subreddit('AskReddit')

# Get the top 100 posts of the month
top_posts = subreddit.top(time_filter='month', limit=100)

# Store the results
posts = []

def filter_comments_by_word_count(comments, min_word_count):
    filtered_comments = [comment for comment in comments if len(comment.body.split()) >= min_word_count]
    return filtered_comments

# Store the results
posts = []

for post in top_posts:
    # Ensure we fetch the top-level comments
    post.comments.replace_more(limit=0)
    
    # Filter comments that have at least 10 words (adjust as needed)
    filtered_comments = filter_comments_by_word_count(post.comments.list(), min_word_count=500)
    
    if filtered_comments:
        # Get the top comment (first comment in the sorted list by upvotes)
        top_comment = max(filtered_comments, key=lambda comment: comment.score)
        description = top_comment.body
    else:
        description = "No top comment with at least 10 words available."

    post_data = {
        'title': post.title,
        'description': description
    }
    posts.append(post_data)

# Print the results
for idx, post in enumerate(posts):
    print(f"{idx + 1}. Title: {post['title']}\nDescription: {post['description']}\n")

# Optionally, you can save the results to a file
import json
with open('top_100_monthly_askreddit_posts.json', 'w') as f:
    json.dump(posts, f, indent=4)
