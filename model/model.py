from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
import numpy as np


#Linear REGRESSION
hours = np.array([1,2,3,4,5,6,7,8,]).reshape(-1,1)
marks = np.array([35,40,50,55,65,70,78,85])

model = LinearRegression()       # create model

model.fit(hours,marks)         # train model

def predict_marks(study_hours):
    prediction = model.predict([[study_hours]])
    return round(prediction[0],2)


# Logistic Regression training data
study_hours = [[1], [2], [3], [4], [5], [6], [7], [8]]
result = [0, 0, 0, 0, 1, 1, 1, 1]


logistic_model = LogisticRegression()


logistic_model.fit(study_hours, result)


def predict_pass_fail(hours):
    prediction = logistic_model.predict([[hours]])

    if prediction[0] == 1:
        return "Pass"
    else:
        return "Fail"
    