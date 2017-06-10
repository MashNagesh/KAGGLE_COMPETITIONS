
# TITANIC SURVIVAL ANALYSIS USING ML TECHNIQUES

### Dataset used

TITANIC DATA - (https://www.kaggle.com/c/titanic/data)

### Objective

To predict the survival state(survived/not survived) of a passenger based on the data provided.

### Brief description

Data contains biological data and socio-economic data for the passengers. The survival status is to be predicted using multiple variables like age, gender, Class of cabin, cost of ticket, port of embarkation. Data cleaning is performed after the outliers are identified and treated appropriately.New features like Adult/Child,Family/solo travel,Binned fares are engineered.

### Algorithms used
<li>DTTitanic.ipynb - Used Decision Trees with default parameters to come up with the Survived variable and gives a score of around 0.71</li>
<li>RFTitanic.ipynb - Used Random forest with parameter tuning using Gridsearchcv and gives a score of 0.746</li>
