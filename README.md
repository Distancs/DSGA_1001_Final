# DSGA_1001_Final

Dras_Dynamic_Rating_Adjustment_System

## Data Cleaning (Raw)

### The final version of Data Cleaning can be found as 'final_version_yeah.csv' in data folder.

All data are fetched from imdb Database and imdbPro Database. 11116 records are selected for BoxOffice Prediction.

There are 41 features including a dummy matrix indicating the genre of each movie. The unique key for each movie is 'Title'. 

4 Actors, 1 director, 1 writter are saved for nlp weight analysis. Ratings from 3 different objective organizations and 1 subjective imdbRating are used to allocate weights. 

The BoxOffice is adjuested by inflation rate.


## Model And Evaluation


The Model part has been uploaded in Model_and_Evaluation notebook.

1. Combined Data in FINAL_version_advanced_adj_score.csv and final_version_yeah.csv to produce data_combined.csv. All models are based on this combined data set.

2. Clearly we have a regression problem. The Response is the 'Adjusted_BoxOffice' instead of raw BoxOffice.

   Baseline model 1: Simple LR with 4 features year, genre(dummy), Runtime, CountryCount. Out-of-sample-Rsq (oosr) = 13
   Baseline model 2: Simple LR with above features and all the raw ratings. Out-of-sample Rsq = 28. This is the model with (serious) data leakage.
   Baseline model 1 is the one we need to beat and Baseline 2 is the model we try to catch up. 
   
   Improved Model 1: Simple LR, with useless feature discarded (by P value) and NLP_Score included, oosr = 20.4
   Improved Model 2: RegressionTree with cross-validation on all features except raw ratings. oosr = 16.8
   Improved Model 3: NN on all features except raw ratings, oosr = 23.6
   
3. Conclusion: With our NLP_Score and appropriate model (appears to be NN here), we can capture (23.6-13)/(28-13) = 75.7% of the variance that can previously be explained only by raw-ratings, which is not available prior to movie release. So in terms of model it is quite successful.

However, BoxOffice has huge variance and remains difficult to predict. Even we use future information (like votes and scores), we can only explain 28% of the variance. We can see this also in the fact that for all models, in sample R2 is always lower than out of sample R2. Perhaps we need to find more features to impove the model a bit at this point.




  
