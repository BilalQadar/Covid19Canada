# Epidemiological Data from the COVID-19 Outbreak in Canada
Using publically available data and machine learning to predict the spread of COVID-19 in Canada throughout time. 

# Disclaimer
The goal of this project was to attempt to model the spread of COVID-19 in Canada using Machine Learning. However, many assumptions were made about the population growth of Canada. The viruses transmission evolves every day resulting in the training data to become outdated very quickly. Take this project as an interesting look at how the virus may change over time and as a potential way of seeing where in the pandemic cycle Canada is. Refer to the [CDC](https://www.cdc.gov/coronavirus/2019-nCoV/index.html), the [WHO](https://www.who.int/emergencies/diseases/novel-coronavirus-2019) and the [Canadian government](https://www.canada.ca/en/public-health/services/diseases/2019-novel-coronavirus-infection/health-professionals/epidemiological-summary-covid-19-cases.html) for up to date and accurate announcements about the current situation in Canada. 

# Results
The figures folder contains all findings. The visualization folder contains figures based on real time data of cases, deaths and recoveries. These figures model the pandemic through time. The number of new cases over time is shown below. 

![New cases over time](https://github.com/BilalQadar/Covid19Canada/blob/master/figures/pandemic%20visualization/new.png)

The number of new cases per day is slowly decreasing showing that social distancing is effectively decreasing the transmission. This is observed through the smaller 'jumps' from day to day. The number of resolved cases is increasing but this largely attributed to 'waves' of people fully recovering 14 days later. ie) If there was a large influx of new cases, its expected there will be a large number of recoveries 10 days later. 

![Resolved cases over time](https://github.com/BilalQadar/Covid19Canada/blob/master/figures/pandemic%20visualization/resolved.png)

The number of active cases is the total number of unresolved cases in Canada at any given time. This is a figure which provides an indication of where in the pandemic cycle Canada currently is.

![Active cases over time](https://github.com/BilalQadar/Covid19Canada/blob/master/figures/pandemic%20visualization/active.png)

All the figures above are based on real data. The next section will manipulate that data and make predictions. As mentioned in the disclaimer all figures below **do not** accurately project infections. 

The model used to predict future infections is based on the SIR (suseptible, infected and recovered) model. This model splits the total population (N) into a suseptible, infected and recovered population. The model assumes that the population remains fixed (the birth rate and death rate are equivalent). Another assumption made is once a persons case is marked resolved they can't become infected again. 

Within the model there are three constants which depend on the virus being studied. These constants are called b, N, gamma and Beta. The constant b refers to the birth rate (and death rate) of the virus. N is the total population of Canada. Furthermore that means our infected, recovered and suseptible populations must always equal to N. Gamma is the probability of recovery from COVID-19. Furthermore, 1 divided by gamma is the average length of infection. Beta is probability of contracting COVID-19. R0 is a constant in which Beta can be derived. R0 refers to the number of people an infected person passes the virus to. R0 is refered to as the basic reproduction number. Using the previous data the R0 and gamma values can be calculated through time. 

![R0 value over time](https://github.com/BilalQadar/Covid19Canada/blob/master/figures/simulation/r0.png)
![Gamma value over time](https://github.com/BilalQadar/Covid19Canada/blob/master/figures/simulation/gamma.png)

Using this previous data of coefficent values a linear regression can be performed. The data was split 70 training and 30 test. This allowed a prediction of the coefficent values in the future. As a result the simulated number of future cases of COVID-19 is displayed below. 

![Simulated cases over time](https://github.com/BilalQadar/Covid19Canada/blob/master/figures/simulation/simulated.png)

# Citation
COVID-19 Canada Open Data Working Group. Epidemiological Data from the COVID-19 Outbreak in Canada. https://github.com/ishaberry/Covid19Canada. (Access Date). 

# Accurate as of: 
April 4th, 2020
