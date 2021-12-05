import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
import numpy as np
import pickle
import warnings

def shorten_categories(categories, cutoff):
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] = 'Other'
    return categorical_map

def clean_experience(x):
    if x ==  'More than 50 years':
        return 50
    if x == 'Less than 1 year':
        return 0.5
    return float(x)

def clean_education(x):
    if 'Bachelor’s degree' in x:
        return 'Bachelor’s degree'
    if 'Master’s degree' in x:
        return 'Master’s degree'
    if 'Professional degree' in x or 'Other doctoral' in x:
        return 'Post grad'
    return 'Less than a Bachelors'

warnings.filterwarnings("ignore")

# df = pd.read_csv("survey_results_public.csv")

df = pd.read_csv('https://alisayezdocker.s3.eu-west-1.amazonaws.com/survey_results_public.csv')
df = df[["Country", "EdLevel", "YearsCodePro", "Employment", "ConvertedComp"]]
df = df.rename({"ConvertedComp": "Salary"}, axis=1)
df = df[df["Salary"].notnull()]
df = df.dropna()
df.isnull().sum()
df = df[df["Employment"] == "Employed full-time"]
df = df.drop("Employment", axis=1)
df['Country'].value_counts()
country_map = shorten_categories(df.Country.value_counts(), 400)
df['Country'] = df['Country'].map(country_map)
df.Country.value_counts()
df = df[df["Salary"] <= 250000]
df = df[df["Salary"] >= 10000]
df = df[df['Country'] != 'Other']

df['YearsCodePro'] = df['YearsCodePro'].apply(clean_experience)
df['EdLevel'] = df['EdLevel'].apply(clean_education)
le_education = LabelEncoder()
df['EdLevel'] = le_education.fit_transform(df['EdLevel'])
le_country = LabelEncoder()
df['Country'] = le_country.fit_transform(df['Country'])
X = df.drop("Salary", axis=1)
y = df["Salary"]

random_forest_reg = RandomForestRegressor(random_state=0)
random_forest_reg.fit(X, y.values)

y_pred = random_forest_reg.predict(X)
error = np.sqrt(mean_squared_error(y, y_pred))

X = np.array([["United States", 'Master’s degree', 15 ]])
X[:, 0] = le_country.transform(X[:,0])
X[:, 1] = le_education.transform(X[:,1])
X = X.astype(float)
y_pred = random_forest_reg.predict(X)

data = {"model": random_forest_reg, "le_country": le_country, "le_education": le_education}
with open('saved_steps.pkl', 'wb') as file:
    pickle.dump(data, file)

print("Model is created")