# Methods

# Prediction Problem

## Research Question Formulation

### Objective

The objective of this paper will be to study the performance of different top sentiment analysis models on Reddit posts. Specifically, this study focuses on r/WallStreetBets (WSB), a subreddit with over 14 million members known for its finance and trading content. The community is infamous for causing market fluctuations on “meme stocks,” stocks that garner intense but momentary interest (Nobanee & Ellili, 2023). The top of these stocks was Gamestop in 2021, where WSB members invoked a short squeeze.

### Significance

While past studies investigated applying sentiment analysis to social media platforms, they’re usually performed on independent individuals rather than groups (Rodríguez-Ibánez et al., 2023; Suhaimin et al., 2023). When analyzing posts made in a community, it is important to note common tendencies and terminology. On WSB, fabricated words like “Paperhands” and “Diamondhands” describe the user’s intended trading decision. By understanding the consensus sentiment, models can perform better price predictions on assets tracked by the subreddit.

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

## References

Barbieri, F., Camacho-Collados, J., Neves, L., & Espinosa-Anke, L. (2020). TWEETEVAL: Unified Benchmark and Comparative Evaluation for Tweet Classification. https://arxiv.org/pdf/2010.12421.pdf

Hutto, C. J., & Gilbert, E. (2014). VADER: A Parsimonious Rule-Based Model for Sentiment Analysis of Social Media Text. Proceedings of the International AAAI Conference on Web and Social Media, 8(1). https://ojs.aaai.org/index.php/ICWSM/article/view/14550

Nobanee, H., & Ellili, N. O. D. (2023). What do we know about meme stocks? A bibliometric and systematic review, current streams, developments, and directions for future research. International Review of Economics & Finance, 85, 589–602. https://doi.org/10.1016/j.iref.2023.02.012

Rodríguez-Ibánez, M., Casánez-Ventura, A., Castejón-Mateos, F., & Cuenca-Jiménez, P.-M. (2023). A Review on Sentiment Analysis from Social Media Platforms. Expert Systems with Applications, 223, 119862. https://doi.org/10.1016/j.eswa.2023.119862

Sanh, V., Debut, L., Chaumond, J., & Wolf, T. (2019). DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter. ArXiv.org. https://arxiv.org/abs/1910.01108

Suhaimin, M., Hijazi, A., Ervin Gubin Moung, Puteri N. E. Nohuddin, Chua, S., & Coenen, F. (2023). Social Media Sentiment Analysis and Opinion Mining in Public Security: Taxonomy, Trend Analysis, Issues and Future Directions. Journal of King Saud University - Computer and Information Sciences, 35(9), 101776–101776. https://doi.org/10.1016/j.jksuci.2023.101776

Xu, Q. A., Chang, V., & Jayne, C. (2022). A systematic review of social media-based sentiment analysis: Emerging trends and challenges. Decision Analytics Journal, 3, 100073. https://doi.org/10.1016/j.dajour.2022.100073

