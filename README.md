# DSGA_1001_Final

Dras_Dynamic_Rating_Adjustment_System

## Data Cleaning (Raw)

### The final version of Data Cleaning can be found as 'final_version_yeah.csv' in data folder.

All data are fetched from imdb Database and imdbPro Database. 11116 records are selected for BoxOffice Prediction.

There are 41 features including a dummy matrix indicating the genre of each movie. The unique key for each movie is 'Title'. 

4 Actors, 1 director, 1 writter are saved for nlp weight analysis. Ratings from 3 different objective organizations and 1 subjective imdbRating are used to allocate weights. 

The BoxOffice is adjuested by inflation rate.
