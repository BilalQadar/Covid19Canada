import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime
from growth_rates import *

def update_values(s, i, r, model, iteration_r, iteration_g):
    r_slope, r_int, ga_slope, ga_int  = model
    R0 = predict_rate(r_slope, r_int, iteration_r)[0][0]
    if R0 < 0:
        R0 = 0
    # Birth Rate and death rate in Canada
    b = 4.2*(10**-5)
    # Infection rate
    ga = predict_rate(ga_slope, ga_int, iteration_g)[0][0]

    # Recovery rate
    be = R0 * (ga + b)
    N = 37.5 * (10**6)

    print('be:', be)
    print('ga: ', ga)
    print('R0: ', R0)
    # Suseptible population
    sp = s + (-1 * (be/N) * i * s) + (b *  (i + r))
    # Infected population
    ip = i * (1 - ga - b) + ((be/N) * i * s)
    # Recovered population
    rp = r*(1-b) + ga * i

    return (sp, ip, rp)

def simulate(cases, mortality, recovered):

    new_cases, immune, deaths, active = active_cases(cases, mortality, recovered)

    x1, r0  = get_r0(cases, mortality, recovered)
    x2, ga0  = get_gamma(cases, mortality, recovered)
    days_r = x1[-1]
    days_g = x2[-1]

    r_slope, r_int = linear_regression(x1, r0)
    ga_slope, ga_int = linear_regression(x2, ga0)
    model = (r_slope, r_int, ga_slope, ga_int)

    N = 37.5 * (10**6)
    s = N - total_cases(new_cases)
    i = active[-1]
    r = 0
    iterations = 0

    x = []
    y = []

    while i != 0:
        x.append(iterations)
        y.append(i)
        iterations += 1
        sp,ip,rp = update_values(s,i,r, model, days_r + iterations, days_g + iterations)

        if int(sp) < 0:
            s = 0
        else:
            s = int(sp)

        if int(ip) < 0:
            i = 0
        else:
            i = int(ip)

        r = int(rp)
        if iterations % 14 == 0:
            print('s:', s)
            print('i:',i)
            print('r:', r, '\n')

    plt.scatter(x,y)
    plt.title('Simulated COVID-19 in Canada')
    plt.xlabel('Number of days since April 4, 2020')
    plt.ylabel('Simulated Number of Canadian citizens infected')
    plt.show()

if __name__ == '__main__':
    cases = pd.read_csv('./datasets/cases.csv')
    mortality = pd.read_csv('./datasets/mortality.csv')
    recovered = pd.read_csv('./datasets/recovered_cumulative.csv')
    simulate(cases, mortality, recovered)
