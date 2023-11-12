# Run to install packages
# pip install praw requests beautifulsoup4

import praw
import requests
from bs4 import BeautifulSoup

# Set up your Reddit API credentials
reddit = praw.Reddit(
    client_id='your_client_id',
    client_secret='your_client_secret',
    user_agent='your_user_agent',
)

# Define the subreddit and keyword
subreddit_name = 'wallstreetbets'
keyword = 'Solana OR SOL'

# Get subreddit instance
subreddit = reddit.subreddit(subreddit_name)

# Search for posts containing the keyword
posts = subreddit.search(query=keyword, sort='new', time_filter='all')

# Initialize lists to store data
upvotes_list = []
comments_list = []
post_content_list = []

# Loop through the posts
for post in posts:
    upvotes_list.append(post.score)
    comments_list.append(post.num_comments)
    
    # Extract post content using BeautifulSoup and Reddit's HTML structure
    post_url = f'https://www.reddit.com{post.permalink}'
    post_html = requests.get(post_url, headers={'User-agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(post_html.text, 'html.parser')
    post_content_list.append(soup.find('div', class_='md').get_text())

# Create a dataset or print the results
dataset = list(zip(upvotes_list, comments_list, post_content_list))
for data in dataset:
    print(data)
