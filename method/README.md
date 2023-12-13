# Methods

## Prediction Problem

## Research Question Formulation

### Objective

This paper aimed to examine how different sentiment analysis models performed on Reddit posts. I specifically looked at r/WallStreetBets (WSB), a subreddit with over 14 million members known for finance and trading discussions. WSB was infamous for influencing market fluctuations, especially in "meme stocks" that attracted intense but short-lived interest (Nobanee & Ellili, 2023). The GameStop short squeeze in 2021, orchestrated by WSB members, was a key example.

I compared various sentiment analysis models to understand how well they captured sentiment in WSB discussions about finance, trading, and meme stocks. The goal was to see which models could best analyze the emotional tone in these posts.

In addition to evaluating model performance, I explored how sentiment in WSB may have affected market participants, regulators, and the wider financial community. Understanding the impact of online sentiment on financial markets is crucial for managing potential risks associated with social media influence.

This research contributed to the discussion on sentiment analysis, focusing on its application in online financial communities like WSB. By studying WSB and its influence on meme stocks, I hoped to shed light on the relationship between online sentiment, trading strategies, and market dynamics, providing insights into the changing landscape of modern finance.

### Significance

Prior research has delved into the application of sentiment analysis on various social media platforms; however, these studies typically focused on individual users rather than cohesive groups (Rodríguez-Ibánez et al., 2023; Suhaimin et al., 2023). A notable gap in the literature exists regarding the nuanced dynamics of sentiment within communal spaces, where collective behavior and shared terminology play a pivotal role. This study aims to address this gap by examining sentiment within the context of online communities, with a particular emphasis on the WallStreetBets (WSB) subreddit.

When analyzing posts within a community setting, it becomes crucial to recognize prevalent tendencies and the emergence of community-specific terminology. On WSB, for instance, participants commonly employ fabricated words such as "Paperhands" and "Diamondhands" to articulate their intended trading decisions. The adoption and shared understanding of these terms contribute to the formation of a unique linguistic ecosystem within the community. Understanding these communal expressions are integral to deciphering sentiment accurately, as they encapsulate the collective sentiment and market outlook of WSB participants.

Beyond linguistic nuances, investigating the consensus sentiment within online communities like WSB holds significant implications for refining predictive modeling, particularly in the context of asset price predictions. By discerning the prevailing sentiment within the community, sentiment analysis models can enhance their ability to forecast price movements and trends associated with assets frequently discussed on the subreddit.
## Operational Measures

### Variables

The independent variable (X) of this study is the textual content of the posts, and the dependent variable (Y) will be the labels given to each post. The sample space of Y is {-1,0,1}, where -1, 0, and 1 correspond to negative, neutral, and positive posts, respectively.

### Data Type

The dataset will contain time-series data, with each post being an observation in a sequence over time. Instead of analyzing each user, the focus is to track sentiment variations on WSB.

## Hypothesis Development

### Prediction Hypothesis

Although numerous models can accurately predict social media sentiment, the performance will significantly decrease when used to analyze WSB posts. Reddit post’s characteristics—short post title and content length, illogical grammatical usage, and the invention of new terminology—will be strongly correlated to the decrease in model performance.

### Justification

Most sentiment analysis models are based on assigning intensity values to words from the standardized English dictionary. This means, however, that they are not programmed to account for unknown variables such as “trendy” words and emoticons. Also, the short post length severely restricts the amount of information each model has to work with, and I believe this will lead to an increased volatility in results. Overall, these three factors should be negatively correlated to model performance.

### Machine Learning Algorithm Selection

As the study focuses on predicting WSB post sentiment, the selected machine learning algorithms utilized natural language processing (NLP) techniques, known to be the most effective in analyzing textual content for sentiment analysis. VaderSentiment uses parsimonious rule-based modeling, allowing for their engine to "work well on social media style text, yet readily generalizable to multiple domains" (Hutto & Gilbert, 2014). Twitter-RoBERTa-base modifies RoBERTa to incorporate emotional, emoji, irony, and hate speech recognition (Barbieri et al., 2020). distilRoberta-financial-sentiment is a finetuned version of DistilRoberta, a more efficient alternative to BERT (Sanh et al., 2019).

## The Machine Learning Workflow

## Model Development

### Data Processing

#### Data Collection

Posts were obtained by scraping the subreddit for textual content, ID, and post popularity (upvotes and comments).

#### Post Quality

The dataset’s quality is ensured by filtering posts on the following threshold:

  T=1 if U,C > 10000; 0 otherwise

where T is the indicator thresholding function, U is the number of upvotes, and C is the number of comments.

#### Labeling

To perform prediction on the self-made dataset, I manually labeled the data. The sample space of the true labels is {-1,0,1}, representing negative, neutral, and positive, respectively.

## Results Presentation

### Training and Testing

#### Dataset Split

Since I can determine the number of posts to use, the dataset was split 85-15 for training and testing. 

#### Results

The result of these models is an array of integers in the subset {-1,0,1}. Each index in the array corresponds to a post’s sentiment from the input information.

### Data Visualization

To visualize the results, I used bar graphs, comparing each model’s accuracy from its respective research to the accuracy when running on the new dataset. I also created bar graphs for each of the three extracted features, separating the data by emoji, model, and ambiguous word respectively.

## Model Evaluation

### Evaluation Criteria

I used accuracy to evaluate the performance of each model and compared it for each of the features. The accuracy was then evaluated with 0.80 as an acceptable performance.

### Iterative Improvement

To accurately predict WSB sentiment, the models need to be adjusted to account for the unknown terminology. I came up with three methods for accomplishing this:

- Amending dictionary: The most direct approach to predict WSB sentiment will be manually adding and assigning intensity values for each unknown word.
- Hypersensitivity: Since sentiment analysis models are designed for longer strings, amplifying the intensity of each word or emoji might improve the model’s accuracy.
- Utilize comments: While comments can be very short, combining (2) with a post’s comments might provide additional context to supplement the post’s brief content.


## References

Barbieri, F., Camacho-Collados, J., Neves, L., & Espinosa-Anke, L. (2020). TWEETEVAL: Unified Benchmark and Comparative Evaluation for Tweet Classification. https://arxiv.org/pdf/2010.12421.pdf

Hutto, C. J., & Gilbert, E. (2014). VADER: A Parsimonious Rule-Based Model for Sentiment Analysis of Social Media Text. Proceedings of the International AAAI Conference on Web and Social Media, 8(1). https://ojs.aaai.org/index.php/ICWSM/article/view/14550

Nobanee, H., & Ellili, N. O. D. (2023). What do we know about meme stocks? A bibliometric and systematic review, current streams, developments, and directions for future research. International Review of Economics & Finance, 85, 589–602. https://doi.org/10.1016/j.iref.2023.02.012

Rodríguez-Ibánez, M., Casánez-Ventura, A., Castejón-Mateos, F., & Cuenca-Jiménez, P.-M. (2023). A Review on Sentiment Analysis from Social Media Platforms. Expert Systems with Applications, 223, 119862. https://doi.org/10.1016/j.eswa.2023.119862

Sanh, V., Debut, L., Chaumond, J., & Wolf, T. (2019). DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter. ArXiv.org. https://arxiv.org/abs/1910.01108

Suhaimin, M., Hijazi, A., Ervin Gubin Moung, Puteri N. E. Nohuddin, Chua, S., & Coenen, F. (2023). Social Media Sentiment Analysis and Opinion Mining in Public Security: Taxonomy, Trend Analysis, Issues and Future Directions. Journal of King Saud University - Computer and Information Sciences, 35(9), 101776–101776. https://doi.org/10.1016/j.jksuci.2023.101776

Xu, Q. A., Chang, V., & Jayne, C. (2022). A systematic review of social media-based sentiment analysis: Emerging trends and challenges. Decision Analytics Journal, 3, 100073. https://doi.org/10.1016/j.dajour.2022.100073

