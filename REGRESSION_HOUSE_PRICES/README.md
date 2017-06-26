# PREDICTION OF HOUSE PRICES USING THE AMES DATASET

The Ames dataset contains the variables (around 80) which determine the sale price of a house.
Details in the link below
<https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data>

### Objective
To predict the Sale price of a house based on these variables.Clear case of Regression

### Procedure adopted
Regression_House_Prices.ipynb - uses Lasso regression
NaN values are replaced with zeros and MISSING tags and log transformations and quadratic transformations are performed for skewed variables.
ANOVA is used to check the impact of variables on Sale price and the feature variables are reduced accordingly based on their impact.
Target based encoding (sorting the categories based on mean of saleprice).
Spearmans coefficient is used to further filter the features and Lasso method is applied.

RidgeCV_Extensive_EDA.ipynb - Ridge CV method
NaN columns addressed as above. Year of Sale is valiadted to be lesser than or equal to date of construction or remodelling.
Sale price Outlier values removed in training data.
Features with a wide scale are simplified and ordinal features are encoded with numbers.
Combination of features are formed and polynomial features are formed based on thier imapct on sale price.
Skewness adjusted using log and dummy variables created for categorical.
RidgeCV algorithm is used and CV score is used for checking the performance.
