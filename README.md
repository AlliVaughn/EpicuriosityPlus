# Epicuriosity 
## Hosted at [Heroku](https://epi-plus.herokuapp.com/)
 
 ## Project Brief 

The Epicuriousity project analyzes the epirecipes dataset found on Kaggle that contains over 20k Epicurious recipes with their ratings, categories and nutritional information.  We used this dataset to understand the popularity of recipes in relation to nutritional information, number of ingredients and categories.

Project Members
Amy Koldeway, Sarah Cross, Alli Vaughn

Data Set
Link to dataset: https://www.kaggle.com/hugodarwood/epirecipes




 ## EPI Factor Math Description

EPI-FACTOR (Normalized Data)

XNORMAL = (XAVG – XMIN) / (XMAX – XMIN)

Where, data is binned for each star rating (0 to < 1, 1 to < 2, etc.)):

XNORMAL = normalized average calories (per rating bin)
XAVG = average calories (per rating bin)
XMIN = minimum overall calories
XMAX = maximum overall calories

Each Radar Chart represents the data grouped by average star rating. This allows you to quickly compare how each value changes with star rating.

Calories (normalized, cal)
Fat (g)
Protein(g)
Number of Ingredients

Data Cleaning

def get_epifactor(min_val, max_val, mean_val):
    return ((mean_val - min_val) / (max_val - min_val)) * 100