# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 18:24:04 2019

@author: Latifah
"""

import pandas as pd

data = pd.read_csv("FuelConsumptionCo2.csv")

## MODELLING MULTIPLE REGRESSION. Variabel Enginsize dan Cylinder terhadap CO2Emmisions ##
X = data[['ENGINESIZE','CYLINDERS']]
Y = data['CO2EMISSIONS']

#from sklearn.model_selection import train_test_split
from sklearn.cross_validation import train_test_split 
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, 
                                                    random_state=4) 

from sklearn import linear_model
reg = linear_model.LinearRegression() 
reg.fit(X_train, Y_train)

print('Intercept: ', reg.intercept_)
print('Coefficients: \n', reg.coef_)
# variance score: 1 means perfect prediction 
print('Variance score: {}'.format(reg.score(X_test, Y_test)))


#%%
x = data[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_CITY','FUELCONSUMPTION_HWY','FUELCONSUMPTION_COMB','FUELCONSUMPTION_COMB_MPG']]
y = data['CO2EMISSIONS']

from sklearn.cross_validation import train_test_split 
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, 
                                                    random_state=4) 

from sklearn import linear_model
regr = linear_model.LinearRegression() 
regr.fit(x_train, y_train)

print('Intercept: ', regr.intercept_)
print('Coefficients: \n', regr.coef_)
# variance score: 1 means perfect prediction 
print('Variance score: {}'.format(regr.score(x_test, y_test)))


#%%
import statsmodels.formula.api as smf

model = smf.ols('CO2EMISSIONS ~ ENGINESIZE', data=data)
result = model.fit()

print("Parameter OLS dgn library:\n", result.params)

#%%

import numpy as np
import matplotlib.pyplot as plt 

# b0 DAN b1 DENGAN OLS #
def estimate_coef(x, y): 
    # number of observations/points 
    n = np.size(x) 
  
    # mean of x and y vector 
    m_x, m_y = np.mean(x), np.mean(y) 
  
    # calculating cross-deviation and deviation about x 
    SS_xy = np.sum(y*x) - n*m_y*m_x 
    SS_xx = np.sum(x*x) - n*m_x*m_x 
  
    # calculating regression coefficients 
    b_1 = SS_xy / SS_xx 
    b_0 = m_y - b_1*m_x 
  
    return(b_0, b_1) 
  
def plot_regression_line(x, y, b): 
    # plotting the actual points as scatter plot 
    plt.scatter(x, y, color = "m", 
               marker = "o", s = 30) 
  
    # predicted response vector 
    y_pred = b[0] + b[1]*x 
  
    # plotting the regression line 
    plt.plot(x, y_pred, color = "g") 
  
    plt.xlabel('x') 
    plt.ylabel('y')
    plt.show() 
  
def main(): 
    # observations 
    x = data['ENGINESIZE']
    y = data['CO2EMISSIONS'] 
  
    # estimating coefficients 
    b = estimate_coef(x, y) 
    print("Estimated coefficients OLS:\nb_0 = {} \
    \nb_1 = {}".format(b[0], b[1]))
  
    # plotting regression line 
    plt.title('OLS', fontsize=15)
    plot_regression_line(x, y, b) 
    
  
if __name__ == "__main__": 
    main() 


# b0 DAN b1 DENGAN DATA TRAIN #
data1 = data[['ENGINESIZE','CO2EMISSIONS']]
msk = np.random.rand(len(data)) < 0.8
train = data1[msk]
test = data1[~msk]

from sklearn import linear_model
regr = linear_model.LinearRegression()
train_x = np.asanyarray(train[['ENGINESIZE']])
train_y = np.asanyarray(train[['CO2EMISSIONS']])
regrs = linear_model.LinearRegression() 
regrs.fit(train_x, train_y)

print('Intercept (b_0) = ', regrs.intercept_)
print('Coefficients (b_1) = ', regrs.coef_)

plt.scatter(train_x, train_y,  color='blue')
plt.plot(train_x, regrs.coef_[0][0]*train_x + regrs.intercept_[0], '-r')
plt.title('Data Train', fontsize=15)
plt.xlabel("Engine size")
plt.ylabel("Emission")
plt.show()
