I have started a new course on Kaggle, on machine learning and the following document contains my notes from the course. All credits are given to Kaggle.

## Decision Tree

Important terms : 

- Fitting / Training : The step of capturing patterns from data is called fitting or training the model.
- Training Data: The data that is used to fit the model is called the training data.
- Prediction : Pretty obvious :P 
- Leaf : The point at the bottom at which we make a prediction is the leaf.

### Pandas

```python
import pandas as pd
filepath = '../this.csv'
fdata = pd.read_cv(filepath)
fdata.describe()
```

The last line gives away 8 lines : 

* Count - How many rows have non-missing values.
* Mean , Standard Deviation, min , max and the percentiles (25% , 50% , 75%)

### Predictive Accuracy

The most common mistake made is that they make predictions with their training data and compare those predictions to the target values in the training data.

Prediction measures : If we measure the accuracy for all the 10,000 houses, it would make no sense because some of them are good and some of them are bad. Thus we use **Mean absolute error**

``` python
error = actual - predicted
absolute_error = abs(error)
# And then take a mean of all the error values.
```

A simpler way to do the above is : 

```python
from sklearn.metrics import mean_absolute_error
```



### Underfitting vs Overfitting

**Underfitting:** failure to capture relevant patterns

**Overfitting: ** capturing patterns that won't recur in the future.

Both of them lead to less accurate results.