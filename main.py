import pandas as pd

wine_data = pd.read_csv("C:/Users/diouc/OneDrive/Bureau/Business/Datasets/Wine Review Dataset/winemag-data-130k-v2.csv")

'''print(wine_data.describe())
print(wine_data.shape)
print(wine_data.head())'''

#assigner la colonne 'description' a une variable : il y a deux moyens
desc_column = wine_data.description
#desc_column2 = wine_data['description']
#print(desc_column)

first_description = wine_data.description.iloc[0] #or wine_data.description[0]
#print(first_description)

first_row = wine_data.iloc[0]
#print(first_row)

#print only selected rows
indexes = [1,2,3,4,5,8]
sample_data = wine_data.iloc[indexes]
#print(sample_data)


#variable containing the country, province, region_1 columns with the index 0, 1, 10, and 100
sample_data_2 = wine_data.loc[[0,1,10,100], ['country', 'province', 'region_1']]
#print(sample_data_2)

#variable containing the country, province, region_1 columns with the first 100 rows
sample_data_3 = wine_data.loc[0:99, ['country', 'province', 'region_1']]
#print(sample_data_3)

#only italian wines
sample_data_4 = wine_data.loc[wine_data.country == 'Italy']
#print(sample_data_4)

#DataFrame containing reviews with at least 1 points from Australia or New Zealand.
top_oceania_wines = wine_data.loc[
    wine_data.country.isin(['Australia', 'New Zealand'])
    & wine_data.points >= 1
]
#print(top_oceania_wines)


#list of unique countries
countries = wine_data.country.unique()
#print(countries)

#how often countries appears
countries_appearences = wine_data.country.value_counts()
#print(countries_appearences)

#centered price
centered_price = wine_data.price - wine_data.price.mean()
#print(centered_price)

best_ratings_per_price = wine_data.groupby('price').max('rating')
#print(best_ratings_per_price)

#minimum and maximum prices for each variety of wine
price_extremes = wine_data.groupby('variety').price.agg(['min', 'max'])
#print(price_extremes)

#the most expensive wine varieties
sorted_varieties = price_extremes.sort_values(by=['min', 'max'], ascending=False)
#print(sorted_varieties)

#'points' column data type
points_dtype = wine_data.points.dtype
#print(points_dtype)

#changing 'points' column data type to string
points_string = wine_data.points.astype(str)
#print(points_string.dtype)

#How many reviews are missing a price ?
n_missing_price = pd.isnull(wine_data.price).sum()
#print(n_missing_price)

reviews_per_region = wine_data.region_1.fillna('Unknown').value_counts().sort_values(ascending=False)
#print(reviews_per_region)

#renaming columns
new_wine_data = wine_data.rename(columns={'region_1':'region', 'region_2':'locale'})
print(wine_data.head())

