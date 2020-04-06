from explore import *
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

def get_r0(cases, mortality, recovered):
    new, recovered, deaths, active  = active_cases(cases, mortality, recovered)
    incubation_period = 5
    x = []
    r = []
    count = 0

    # Remove datapoints before social distancing
    outdated = 30
    start = outdated + incubation_period

    for i in range(start,len(new)):
        if new[i-incubation_period] != 0:
            x.append(count)
            r.append(new[i]/new[i-incubation_period])
            count += 1

    #plt.scatter(x,r)
    #plt.show()
    return (x,r)

def get_gamma(cases, mortality, recovered):
    N = 37.5 * (10**6)
    k = 1
    x = []
    ga = []
    total_inf = 0
    total_recovered = 0
    count = 0

    # Irrelevent cutoff refers to when datapoints are recent enough to reflect
    # current enviroment for pandemic. ie) exclude data before social distancing
    cutoff = 40
    new, recovered, deaths, active  = active_cases(cases, mortality, recovered)

    for i in range(len(new)):
        total_inf += new[i]
        total_recovered += recovered[i]
        if i > cutoff:
            ga.append(recovered[i]/total_inf)
            x.append(count)
            count += 1

    #plt.scatter(x,ga)
    #plt.show()
    return (x,ga)

def linear_regression(x_data,y_data):

    x_data = np.asarray(x_data, dtype=np.float32)
    y_data = np.asarray(y_data, dtype=np.float32)

    x_data = x_data.reshape(-1,1)
    y_data = y_data.reshape(-1,1)
    X_train, X_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.2, random_state=0)
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)

    return (regressor.coef_, regressor.intercept_)

def predict_rate(slope, intercept, time):
    """pls don't forget that time is the number of days in the future beyond
    known data """

    return slope*(time) + intercept
