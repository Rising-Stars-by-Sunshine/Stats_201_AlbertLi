This project involved extracting post information from r/WallStreetBets using the PRAW (Python Reddit API Wrapper) library. The main focus was on three key elements: post content, upvotes, and comments. Utilizing Reddit API credentials, PRAW was employed to extract every post from r/WallStreetBets within the past year. The aim was to sort for quality by selecting posts with a minimum of 10000 upvotes and comments. This criterion was chosen to ensure that only posts with sufficient community interaction were included, indicating a potential shift in opinion or sentiment about a specific asset or the market as a whole.

## Data Extraction

The data extraction process involved accessing the Reddit API and retrieving posts meeting the specified criteria. The extracted data included post content, upvote count, and the number of comments for each post. This dataset was then manually labeled to create true labels, which would be used to compare the results of sentiment analysis models.

## Sentiment Analysis Models

After data preparation, three sentiment analysis models were employed to analyze the labeled dataset. The models used were:

1. [VaderSentiment](https://github.com/cjhutto/vaderSentiment#python-demo-and-code-examples): Model designed for sentiment analysis on text data and provides a polarity score for each post.

2. [Twitter-roBERTa-base](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest): Leverages the roBERTa-base architecture, fine-tuned on Twitter data.

3. [distilRoberta-financial-sentiment](https://huggingface.co/mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis): Model fine-tuned specifically for financial sentiment analysis.

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
