import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime

def active_cases(cases, mortality, cured):
    # takes a few days for accurate data to get added to the dataset
    today = datetime.datetime.now().date()
    #cushion_days.append(today - datetime.timedelta(days=i+1))

    # date_dict = {date: [new_cases, deaths, recoveries]}
    date_dict = {}
    active_cases = []
    deaths = []
    recovered = []
    new_cases = []
    active = 0

    for date in cases['date_report']:

        if date in date_dict:
            date_dict[date][0] += 1
        else:
            date_dict[date] = [1,0,0]

    for date in mortality['date_death_report']:

        if date in date_dict:
            date_dict[date][1] += 1
        else:
            date_dict[date] = [0,1,0]

    for i in range(len(cured['date_recovered'])):
        date = cured['date_recovered'][i]
        number_recovered = cured['cumulative_recovered'][i]
        if not pd.isna(number_recovered):
            if date in date_dict:
                date_dict[date][2] += number_recovered
            else:
                date_dict[date] = [0,0,number_recovered]

    iter_dates = [datetime.datetime.strptime(ts, "%d-%m-%Y") for ts in date_dict.keys()]
    iter_dates.sort()
    sorted_dates = [datetime.datetime.strftime(ts, "%d-%m-%Y") for ts in iter_dates]

    for date in sorted_dates:
        daily_insights = date_dict[date]
        new = daily_insights[0]
        death = daily_insights[1]
        recover = daily_insights[2]
        #print(date, ': ', new)
        new_cases.append(new)
        deaths.append(death)
        recovered.append(recover)

        active += new - death - recover
        active_cases.append(active)
        #print(date, ': ', active)

    x_ticks = []
    display_dates = []
    for i in range(len(sorted_dates)):
        if i % 10 == 0:
            display_dates.append(sorted_dates[i][:-5])
            x_ticks.append(i)

    plt.plot(sorted_dates, active_cases, color='red')
    plt.xlabel('Date')
    plt.ylabel('Number of active COVID-19 cases')
    plt.title('Number of active COVID-19 cases with respect to time')
    plt.xticks(x_ticks, display_dates)
    plt.show()
    #
    plt.plot(sorted_dates, new_cases, color='red')
    plt.xlabel('Date')
    plt.ylabel('Number of new COVID-19 cases')
    plt.title('Number of new COVID-19 cases with respect to time')
    plt.xticks(x_ticks, display_dates)
    plt.show()
    #
    # plt.plot(sorted_dates, deaths, color='red')
    # plt.xlabel('Date')
    # plt.ylabel('Number of deaths')
    # plt.title('Number of COVID-19 deaths with respect to time')
    # plt.xticks(x_ticks, display_dates)
    # plt.show()
    #
    # plt.plot(sorted_dates, recovered, color='blue')
    # plt.xlabel('Date')
    # plt.ylabel('Number of recovered COVID-19 caes')
    # plt.title('Number of COVID-19 recoveries with respect to time')
    # plt.xticks(x_ticks, display_dates)
    # plt.show()
    #
    line_1 = plt.plot(sorted_dates, recovered, color='blue')
    line_2 = plt.plot(sorted_dates, deaths, color='red')
    plt.xlabel('Date')
    plt.ylabel('Number of resolved COVID-19 cases')
    plt.title('Number of resolved COVID-19 cases with respect to time')
    plt.legend(['recoveries', 'deaths'])
    plt.xticks(x_ticks, display_dates)
    plt.show()

    return (new_cases, recovered, deaths, active_cases)

def total_cases(new_cases):
    total = 0
    for num in new_cases:
        total += num
    return total
