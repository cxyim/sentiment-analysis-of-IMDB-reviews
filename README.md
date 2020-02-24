# sentiment-analysis-of-IMDB-reviews
Sentiment analysis of Leonardo's film reviews

web crawler: [SeleniumScrapper.py](https://github.com/cxyim/sentiment-analysis-of-IMDB-reviews/blob/master/SeleniumScrapper.py)

data preprocessing and model training: [final.ipynb](https://github.com/cxyim/sentiment-analysis-of-IMDB-reviews/blob/master/final.ipynb)

This project aims to apply the machine learning models to analyse the sentiment of Leonardo’s films.

This project includes several steps:

(1) Data extraction: use WebDriver to crawl movie reviews of Leonardo from IMDB (by selenium library)

(2) Manual label: Select representative films to label Pos or Neg

(3) Text preprocessing: replace contractions, remove non-ascii, remove punctuation, etc.

(4) Model training: Use classification algorithm including random forest, SVM, deep learning, etc.

(5) Compare result of different models

dataset includes: 

| movie | title | rate | author | date | content | label |
| :-----| :-----|:-----|:-----|:-----|:-----|:-----|
| Blood Diamond | One word: Superb | 9/10 | D_Mas | 2007/10/8 | A wonderful movie, wish I would have seen this movie earlier! Blood Diamond brought together a variety of different aspects. | pos |


result: predicted label (pos or neg)
