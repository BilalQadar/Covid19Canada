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
    outdated = 35
    start = outdated + incubation_period

    for i in range(start,len(new)):
        if new[i-incubation_period] != 0:
            x.append(count)
            r.append(new[i]/new[i-incubation_period])
            count += 1

    plt.scatter(x,r)
    plt.title('R0 Values with Canadian COVID-19 Data')
    plt.xlabel('Days since Febuary 30, 2020')
    plt.ylabel('Rate of virus transmission')
    plt.show()
    return (x,r)

def get_gamma(cases, mortality, recovered):
    N = 37.5 * (10**6)
    k = 1
    x = []
    ga = []
    total_inf = 0
    total_recovered = 0
    count = 0

    # Outdated refers to when datapoints which are outdated and don't reflect
    # current enviroment for pandemic. ie) exclude data before social distancing
    outdated = 45
    new, recovered, deaths, active  = active_cases(cases, mortality, recovered)

    for i in range(len(new)):
        total_inf += new[i]
        total_recovered += recovered[i]
        if i > outdated:
            ga.append(recovered[i]/total_inf)
            x.append(count)
            count += 1

    plt.scatter(x,ga)
    plt.title('Gamma Values with Canadian COVID-19 Data')
    plt.xlabel('Days since Febuary 30, 2020')
    plt.ylabel('Probability of recovery from COVID-19')
    plt.show()

    return (x,ga)

def linear_regression(x_data,y_data):

    x_data = np.asarray(x_data, dtype=np.float32)
    y_data = np.asarray(y_data, dtype=np.float32)

    x_data = x_data.reshape(-1,1)
    y_data = y_data.reshape(-1,1)
    regressor = LinearRegression()
    regressor.fit(x_data, y_data)

    return (regressor.coef_, regressor.intercept_)

def predict_rate(slope, intercept, time):
    """pls don't forget that time is the number of days in the future beyond
    known data """

    return slope*(time) + intercept

if __name__ == '__main__':
        cases = pd.read_csv('./datasets/cases.csv')
        mortality = pd.read_csv('./datasets/mortality.csv')
        recovered = pd.read_csv('./datasets/recovered_cumulative.csv')
        get_gamma(cases, mortality, recovered)
        get_r0(cases, mortality, recovered)
