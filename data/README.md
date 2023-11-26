A Python script will be run to prepare the data, leveraging the PRAW (Python Reddit API Wrapper) library to extract post information from r/WallStreetBets. The focus is on three key elements: post content, upvotes, and comments. Using Reddit API credentials, PRAW will extract every post from r/WallStreetBets from the top of the past year. To sort for quality, only the posts with 250 upvotes and comments will be used. This is because posts with sufficient community interaction will indicate a potential shift in opinion or sentiment about a specific asset or the market altogether. The data will then be manually labeled to create a true label to compare the sentiment analysis models results to.

# Data Dictionary

| Variable Name   | Definition           | Description                                    | Frequency | Sample Observation                                      | Type      |
|:---------------:|:---------------------:|-----------------------------------------------|:---------:|:--------------------------------------------------------:|:---------:|
| `post_id`       | Reddit Post ID        | The unique identifier of each post.            | 1000      | "abc123"                                                 | String    |
| `post_title`    | Reddit Title Text      | The title of posts on r/WallStreetBets.        | 1000      | "GME to the moon! 🚀"                                     | String    |
| `post_content`  | Reddit Post Text      | The textual content of posts on r/WallStreetBets. | 1000    | "Just bought more AMC, let's hold strong! 💎🙌"           | String    |
| `comments`      | Number of Comments    | The count of comments on each Reddit post.      | 1000      | 235                                                      | Numeric   |
| `upvotes`       | Upvotes               | The number of upvotes received by each post.    | 1000      | 1879                                                     | Numeric   |


See the [Google Colab Notebook](https://github.com/Rising-Stars-by-Sunshine/Stats_201_AlbertLi/blob/main/data/STATS_201_ajl128_data_query.ipynb). Also see [PRAW](https://praw.readthedocs.io/en/stable/) for more details.

## Prerequisites

1. Install PRAW through pip.
```python
pip install praw
```
2. Obtain Reddit API credentials. See [Reddit API](https://www.reddit.com/dev/api/) for more details.

## Sample Code

```python
import praw
from google.colab import userdata

# Set up PRAW with your Reddit API credentials
reddit = praw.Reddit(
    client_id= userdata.get('clientID'),
    client_secret= userdata.get('clientSecret'),
    user_agent= userdata.get('userAgent')
)

# Specify the subreddit you want to scrape
subreddit_name = 'WallStreetBets'
subreddit = reddit.subreddit(subreddit_name)

# Iterate through the top 5 hot posts in the subreddit
for submission in subreddit.hot(limit=5):
    # Extract relevant information
    post_id = submission.id
    post_title = submission.title
    post_content = submission.selftext
    upvotes = submission.score
    num_comments = submission.num_comments

    # Print or store the information as needed
    print(f"Post ID: {post_id}")
    print(f"Title: {post_title}")
    print(f"Content: {post_content}")
    print(f"Upvotes: {upvotes}")
    print(f"Number of Comments: {num_comments}")
    print("\n" + "-" * 50 + "\n")
```
