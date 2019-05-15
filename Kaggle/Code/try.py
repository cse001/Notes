import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
fp = '../melb_data.csv'
ff = pd.read_csv(fp)
ff = ff.dropna(axis=0)
print (ff.describe())
print (ff.columns)
features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
X = ff[features]
y = ff.Price
print (X.head())
print (X.describe())
mel_model = DecisionTreeRegressor(random_state=1)
mel_model.fit(X,y)
print ("Let's predict")
predicted_values = mel_model.predict(X)
print (mean_absolute_error(predicted_values,y))
# print (mel_model.predict(X.head()))
# print (ff['Price'].head())
train_X , val_X , train_y, val_y = train_test_split(X,y,random_state=1)
mel_model.fit(train_X,train_y)
val_predictions = mel_model.predict(val_X)
print (mean_absolute_error(val_predictions,val_y))
finalModel = DecisionTreeRegressor(ma)
