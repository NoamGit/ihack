# ihack
Supervised model for tagging anti-israeli twitter users based on tweets analysis

### in short -
24 h project (2 men involved)
Used Twitter API for crawling anti-israeli and pro-israli users based on publication of hostile or positive hashtags (Python).
resulting 1500 user_data of each containing maximum - last 300 tweets

### Enginerred features according to -
 - lists of expert's adviced word for different conflict position.
 - timezone utc offset
 - sentiment analysis (using VADER model) of "super tweets"
 reulting 89 dimension feature vec
 
### Training
A decision tree (100 tree 32 depth) and logistic-regression models for binary classification of pro or anti israeli opinion using Azure ML

### Test precision, recall and accuracy results:
![ROC and eval metrics]({{site.baseurl}}//LR_RF_comparison.PNG)

issues - 
 - non balanced data set (80% - 20%)
 - no time for model improvments (CrossVal etc.)
 - model was not exported to web app 
 - key autho problems in tweeter API
 - learn how to export the model
