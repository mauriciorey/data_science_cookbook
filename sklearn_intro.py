from sklearn.datasets import load_iris, load_boston, make_classification
from sklearn.preprocessing import PolynomialFeatures
from sklearn.tree import DecisionTreeClassifier
import numpy as np

#Iris data
data = load_iris()
x = data['data']
y = data['target']
y_labels = data['target_names']
x_labels = data['feature_names']

print x.shape
print y.shape
print x_labels
print y_labels

#Boston data
data = load_boston()
x = data['data']
y = data['target']
x_labels = data['feature_names']

print x.shape
print y.shape
print x_labels

#Make classification dataset
x,y = make_classification(n_samples = 50, n_features = 5, n_classes = 2)
print x.shape
print y.shape
print x[1,:]
print y[1]

#Sklearn functionalities
x = np.asmatrix([[1,2],[2,4]])
poly = PolynomialFeatures(degree = 2)
poly.fit(x)
x_poly = poly.transform(x)

print x.shape
print x_poly.shape

data = load_iris()
x = data['data']
y = data['target']

estimator = DecisionTreeClassifier()
estimator.fit(x,y)
predicted_y = estimator.predict(x)
predicted_y_prob = estimator.predict_proba(x)
predicted_y_lprob = estimator.predict_log_proba(x)

print predicted_y
print predicted_y_prob
print predicted_y_lprob