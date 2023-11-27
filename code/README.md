The code will be comprised of two parts: web scraping and testing. The web scraping portion will be created using PRAW (Python Reddit API Wrapper) to access the Reddit API and to scrape the contents of r/WallStreetBets. From each post, the post's textual content, upvotes, and comments will be extracted. To filter the resultant data, a threshold of 250 comments and upvotes will be applied to ensure the quality of each post. After filtering, I will manually label the data to assign each post as positive, neutral, or negative. For the testing, methodologies from multiple high-performing sentiment analysis models will run the r/WallStreetBets dataset on an 85-15 train-test split. Finally, the results will be compared with the true labels (created manually) to analyze for accuracy, f-measure, precision, and recall.

# Webscraping

See the [Google Colab Notebook](./STATS_201_ajl128_data_query.ipynb). Also see [PRAW](https://praw.readthedocs.io/en/stable/) for more details.

## Prerequisites

1. Install PRAW through pip.
```python
pip install praw
```
2. Obtain Reddit API credentials. See [Reddit API](https://www.reddit.com/dev/api/) for more details.

### Reddit API Setup

1. Create a Reddit account [here](https://www.reddit.com/register/).

2. [Create a Reddit app](https://www.reddit.com/prefs/apps) for personal use. Fill out the name, description, about URL, and redirect URI as desired.
![Create Reddit App](./reddit_api_step_1.png)
3. Extract the "personal use script", "secret", and your application name. These will be your client_id, client_secret, and user_agent.
![Obtain API credentials](./reddit_api_step_2.png)

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

## Flowchart
![Coding Process](./coding-process.png)
