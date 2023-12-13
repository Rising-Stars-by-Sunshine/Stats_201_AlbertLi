# Method: The Machine Learning Workflow

## Model Development

### Data Processing

#### Data Collection

Posts will be obtained by scraping the subreddit for textual content, date, and post popularity. I define post popularity as the number of upvotes and comments a post receives.

#### Post Quality

The dataset’s quality is ensured by filtering posts on the following threshold:

  T=1 if U+C > 250; 0 otherwise

where T is the indicator thresholding function, U is the number of upvotes, and C is the number of comments.

#### Labeling

In order to perform prediction on the self-made dataset, I will manually label the data. The sample space of the true labels is {-1,0,1}, representing negative, neutral, and positive, respectively.

## Results Presentation

### Training and Testing

#### Dataset Split

Since I can determine the number of posts to use, the dataset is split 85-15 for training and testing. 

#### Results

The results of these models will be an array of integers in the subset {-1,0,1}. Each index in the array corresponds to a post’s sentiment from the input information.

### Data Visualization

To visualize the results, I will use heat maps and graphs. I will also use a heatmap 2x2 chart to compare the results of each model to the true labels. I will also use a histogram to compare each model’s accuracy from its respective research to the accuracy when running on the new dataset.

## Model Evaluation

### Evaluation Criteria

Based on the most common metrics obtained from the study by Xu et al. (2022), I will be using accuracy, f-measure, recall, and precision to evaluate the performance of each model. These metrics will be visualized in a table to compare the results with each method.

### Iterative Improvement

In order to accurately predict WSB sentiment, the models need to be adjusted to account for the unknown terminology. I came up with three methods for accomplishing this:

- Amending dictionary: The most direct approach to predict WSB sentiment will be manually adding and assigning intensity values for each unknown word.
- Hypersensitivity: Since sentiment analysis models are designed for longer strings, amplifying the intensity of each word might improve the model’s accuracy.
- Utilize comments: While comments can be very short, combining (2) with a post’s comments might provide additional context to supplement the post’s brief content.

## References

Nobanee, H., & Ellili, N. O. D. (2023). What do we know about meme stocks? A bibliometric and systematic review, current streams, developments, and directions for future research. International Review of Economics & Finance, 85, 589–602. https://doi.org/10.1016/j.iref.2023.02.012

Rodríguez-Ibánez, M., Casánez-Ventura, A., Castejón-Mateos, F., & Cuenca-Jiménez, P.-M. (2023). A Review on Sentiment Analysis from Social Media Platforms. Expert Systems with Applications, 223, 119862. https://doi.org/10.1016/j.eswa.2023.119862

Suhaimin, M., Hijazi, A., Ervin Gubin Moung, Puteri N. E. Nohuddin, Chua, S., & Coenen, F. (2023). Social Media Sentiment Analysis and Opinion Mining in Public Security: Taxonomy, Trend Analysis, Issues and Future Directions. Journal of King Saud University - Computer and Information Sciences, 35(9), 101776–101776. https://doi.org/10.1016/j.jksuci.2023.101776

Xu, Q. A., Chang, V., & Jayne, C. (2022). A systematic review of social media-based sentiment analysis: Emerging trends and challenges. Decision Analytics Journal, 3, 100073. https://doi.org/10.1016/j.dajour.2022.100073
