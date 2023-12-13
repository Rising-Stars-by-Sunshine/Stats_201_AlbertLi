# Sentiment Analysis of r/WallStreetBets

// Poster

## Project Information
- Author: Albert Li, Data Science, Class of 2027, Duke Kunshan University
- Instructor: Prof. Luyao Zhang, Duke Kunshan University
- Disclaimer: Submissions to the Final Project for STATS201 Introduction to Machine Learning for Social Science, 2023 Autumn Term (Seven Week - Second) instructed by Prof. Luyao Zhang at Duke Kunshan University.
- Acknowledgements: I would like to acknowledge Professor Luyao Zhang and my classmates for fostering a collaborative and academically stimulating class environment.

## Project Summary
- Modern sentiment analysis models have proven to accurately predict social media opinions on popular platforms like X (formerly Twitter) and Facebook. However, there is a gap in research into the sentiment analysis of Generation Z (Gen Z) social media, specifically, the usage of ambiguous words, emojis, and newly invented words. This research studies the performance of popular sentiment analysis models on r/WallStreetBets (WSB), a 14-million-member Reddit community infamous for its involvement in the Gamestop short squeeze. In addition, the research analyzes various features like post length, emojis, and ambiguous words. Using the results of this research, future studies will be performed on the optimization of machine learning models for new-generation social media sentiment. Additionally, the scope of future studies will be targeted toward financial sentiment analysis of WSB as a feature for financial asset price prediction.
- The questions this study aims to answer are:
  -  Will popular sentiment models trained for social media analysis return significantly lower performance on a WSB dataset?
  -  Which factors (new words, emojis, ambiguous meanings) affect model performance?

## Application Scenario
- This study’s findings introduce a future area of research for sentiment analysis models: Gen Z’s online communication style. Specifically, it proposes several factors that might help analyze Gen Z's social media sentiment. Understanding Gen Z sentiment is crucial as they account for a third of China’s online population, thereby having a stake in the overall public opinion (Hu et al., 2022). Automating the acquisition of public sentiment will have major impacts in multiple sectors, streamlining the feedback process from individuals to companies, from citizens to governments, and from consumers to producers.

## Methodology
The methodology for this research project can be broken into three processes: data collection, model implementation, and data analysis. Each step can be accessed in this repository's "Code" folder. 
- Data Collection
  - Without a publicly available dataset for WSB, this research begins with data collection and querying. This study utilizes the Python Reddit API Wrapper (PRAW) module, an open-source code library designed to facilitate the usage of the Reddit API. The code sorts the community by its top posts, filtering only for posts with over 10,000 upvotes and comments to ensure post quality and significance, accurately reflecting the community's general sentiment. The data was then manually labeled as positive (1), neutral (0), or negative (-1). The resultant dataset for this study was composed of 955 posts.
- Model Implementation
  - As this research was designed to target social media sentiment, three popular social media sentiment analysis models were used: VaderSentiment (VS), Twitter-roBERTa-base (TRB), and distilRoberta-financial-sentiment (DFS). For sentiment prediction, each model segmented the post string into 128-character chunks to ensure proper model functionality. Each chunk was weighted by its string length and averaged to evaluate the post's sentiment.
- Data Analysis
  - From the data, the average sequence length, top three emojis, and top five ambiguous words were extracted from relevant posts. These results were graphed and compared between models, highlighting the accuracy for each case.
 
## Results
The results indicated that sentiment analysis models indeed struggle in predicting WSB sentiment, with each model obtaining less than 70% accuracy. This result validates the necessity for future focus on this area of research and suggests that the differences between each generation's use of language are strong contributors to this drop in accuracy. The study looked at three of these cases: average post length, emoji usage, and ambiguous word usage. The average post length of the incorrect sequences was on average longer than that of correctly labeled ones, indicating that the models were likely confused by more sharply contrasting sentiments toward different topics. Additionally, the use of emoji had varied effects on model accuracy, with the rocket increasing accuracy and the ape significantly decreasing accuracy. While it is difficult to make conclusive judgments due to the many confounding variables, the posts with rockets likely incorporated more clear sentiment indications, resulting in an overall increase in accuracy. The inverse can be said about the ape, where the posts included conflicting keywords that confused the model. In these cases, the models did not see the proper significance and/or sentiment of the emojis, which commonly have a large impact on a post's sentiment. The use of ambiguous words also had varied effects on model performance, indicating that the ambiguous terms did not significantly impact the post's sentiment.

## Intellectual Merits and Practical Impacts
This research introduces the need for future research into new-generation social media 

## Repository Table of Contents

#### 1. **[Introduction](#introduction)**
#### 2. **[Code](#code)**
#### 3. **[Data](#data)**
#### 4. **[Literature](#literature)**

## Introduction

This project extracted post information from r/WallStreetBets using the PRAW (Python Reddit API Wrapper) library. The main focus was on three key elements: post content, upvotes, and comments. Using Reddit API credentials, PRAW extracted every post from r/WallStreetBets within the past year. The aim was to sort for quality by selecting posts with a minimum of 10000 upvotes and comments. This criterion was chosen to ensure that only posts with sufficient community interaction were included, indicating a potential shift in opinion or sentiment about a specific asset or the market as a whole.

## Code

### Data Extraction

The data extraction process involved accessing the Reddit API and retrieving posts meeting the specified criteria. The extracted data included post content, upvote count, and the number of comments for each post. This dataset was then manually labeled to create true labels, which would be used to compare the results of sentiment analysis models.

### Sentiment Analysis Models

After data preparation, three sentiment analysis models were employed to analyze the labeled dataset. The models used were:

1. [VaderSentiment](https://github.com/cjhutto/vaderSentiment#python-demo-and-code-examples): Model designed for sentiment analysis on text data and provides a polarity score for each post.

2. [Twitter-roBERTa-base](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest): Leverages the roBERTa-base architecture, fine-tuned on Twitter data.

3. [distilRoberta-financial-sentiment](https://huggingface.co/mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis): Model fine-tuned specifically for financial sentiment analysis.

[Folder](https://github.com/Rising-Stars-by-Sunshine/Stats_201_AlbertLi/tree/main/code) containing the various sentiment analysis models from prior high-performing models.

## Data

[Folder](https://github.com/Rising-Stars-by-Sunshine/Stats_201_AlbertLi/tree/main/data) containing the data and the data querying method.

## Literature

[Folder](https://github.com/Rising-Stars-by-Sunshine/Stats_201_AlbertLi/tree/main/literature) containing documentation and literature to elucidate the study's goals and findings.

## Results

### Accuracy Over Epochs

![Combined Results](/results/accuracy-plot.png)

### Accuracy
- VaderSentiment: 0.471204
- Twitter-roBERTa-base: 0.579058
- distilRoberta-financial-sentiment: 0.351832
---
# Resume

## Albert Li

![Headshot](Headshot.jpg)

Albert Li, '27, undecided major.
I'm a freshman at Duke Kunshan University (DKU) with a passion for both STEM and finance, although I haven't settled on a specific major just yet. I'm excited to explore the intersection of these fields and discover where my interests lie. In addition to my academic pursuits, I'm an active member of the DKU Finance Club and the DKU Pre-Law Society, allowing me to engage in discussions related to finance, investment, and economic trends, as well as explore the legal aspects of business and finance. Beyond my club involvement, I'm always seeking new opportunities to broaden my horizons and make meaningful connections on campus, believing that diverse experiences will guide me toward a fulfilling academic and professional journey at DKU.

## Summary
Experienced software developer with a passion for building innovative solutions. Skilled in Python, JavaScript, and React.

## Education
**Bachelor of Science in Data Science**  
Duke Kunshan University, 2027
- GPA: 4.0/4.0
---
**Associate of Science in Computer Science**
Finger Lakes Community College, 2023
- GPA: 4.0/4.0
- Courses: Object-Oriented Software Development, Data Structure, Discrete Mathematics, Computer Architecture, Hardware & Operating Systems, Networking Technologies, Technical Ethics

## Experience
### Software Development Intern | HealthX (2023)
- Sole software development member responsible for architecting and implementing the entire software stack.
- Collaborated with cross-functional teams to deliver scalable and maintainable software solutions.
- Collaborated with startup head and UX designer for website design.
- Developing a Kotlin-based mobile application for seamless integration with wearable devices via Bluetooth technology.
- Implementing real-time data reception from wearable sensors and secure storage in a database.

## Skills
- **Languages:** Python, Java, JavaScript, C++
- **Frameworks:** React, Flutter
- **Tools:** Git
- **Soft Skills:** Team Collaboration, Problem Solving

## Projects
- [HealthX Website]([https://github.com/username/project-a](https://test-8792e6-7860c922f4167-10b3928188638.webflow.io/)): Website for HealthX.


## Contact
- Email: ajl128@duke.edu
- LinkedIn: [https://www.linkedin.com/in/albert-li](https://www.linkedin.com/in/albert-li-6b5412242/)
