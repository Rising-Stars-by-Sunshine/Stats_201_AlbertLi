This project involved extracting post information from r/WallStreetBets using the PRAW (Python Reddit API Wrapper) library. The main focus was on three key elements: post content, upvotes, and comments. Utilizing Reddit API credentials, PRAW was employed to extract every post from r/WallStreetBets within the past year. The aim was to sort for quality by selecting posts with a minimum of 10000 upvotes and comments. This criterion was chosen to ensure that only posts with sufficient community interaction were included, indicating a potential shift in opinion or sentiment about a specific asset or the market as a whole.

## Data Dictionary

| Variable Name   | Definition           | Description                                    | Frequency | Sample Observation                                      | Type      |
|:---------------:|:---------------------:|-----------------------------------------------|:---------:|:--------------------------------------------------------:|:---------:|
| `post_id`       | Reddit Post ID        | The unique identifier of each post.            | 1000      | "abc123"                                                 | String    |
| `post_title`    | Reddit Title Text      | The title of posts on r/WallStreetBets.        | 1000      | "GME to the moon! 🚀"                                     | String    |
| `post_content`  | Reddit Post Text      | The textual content of posts on r/WallStreetBets. | 1000    | "Just bought more AMC, let's hold strong! 💎🙌"           | String    |
| `comments`      | Number of Comments    | The count of comments on each Reddit post.      | 1000      | 2340                                                      | Numeric   |
| `upvotes`       | Upvotes               | The number of upvotes received by each post.    | 1000      | 88234                                                     | Numeric   |

## Flowchart
![Data Dictionary](./data-dictionary.png)
