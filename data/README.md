A Python script will be run to prepare the data, leveraging the PRAW (Python Reddit API Wrapper) library to extract post information from r/WallStreetBets. The focus is on three key elements: post content, upvotes, and comments. Using Reddit API credentials, PRAW will extract every post from r/WallStreetBets from the top of the past year. To sort for quality, only the posts with 250 upvotes and comments will be used. This is because posts with sufficient community interaction will indicate a potential shift in opinion or sentiment about a specific asset or the market altogether. The data will then be manually labeled to create a true label to compare the sentiment analysis models results to.

**Data Dictionary**

| Variable Name    | Definition            | Description                                       | Frequency | Range   | Unit   | Type      |
|:-----------------:|:----------------------:|---------------------------------------------------|:---------:|:-------:|:------:|:---------:|
| `post_text`       | Reddit Post Text      | The textual content of posts on r/WallStreetBets. |1000       |N/A      |N/A     | String    |
| `comments`        | Number of Comments     | The count of comments on each Reddit post.         |1000       | Integer |N/A     | Numeric   |
| `upvotes`         | Upvotes               | The number of upvotes received by each post.      |1000       | Integer |N/A     | Numeric   |

**Sample Code**
![Open In nbviewer](https://nbviewer.org/github/Rising-Stars-by-Sunshine/Stats_201_AlbertLi/blob/main/data/STATS_201_ajl128_data_query.ipynb)
