# Epidemiological Data from the COVID-19 Outbreak in Canada
Used publically available data to attempt to predict the amount of time before Canada will have 0 COVID-19 cases. Mathematical model used was the SIR model with the assumption that once infected and recovered the human is no longer suseptible. Furthermore, used machine learning (linear regressions) to predict future R0, gamma and beta values for the virus. 

# Disclaimer
This project was a method of simulating COVID-19 over time. However, many assumptions were made about the population growth of Canada. The viruses transmission evolves every day causing the data used to model the virus coffecients becomes outdated quite quickly. Take this project as an interesting look at how the virus may change over time and as a potential way of seeing where in the pandemic cycle Canada is. Refer to the CDC, the WHO and the Canadian government for accurate announcements about the current situation in Canada. 

# Results
The figures folder contains all findings. The visualization folder contains figures based on real time data of cases, deaths and recoveries. These figures model the pandemic through time. The number of new cases over time is shown below. 

![New cases over time](https://github.com/BilalQadar/Covid19Canada/blob/master/figures/pandemic%20visualization/new.png)

The number of new cases per day is slowly decreasing showing that social distancing is effectively decreasing the transmission. This is observed through the smaller 'jumps' from day to day. The number of resolved cases is increasing but this largely attributed to 'waves' of people fully recovering 14 days later. ie) If there was a large influx of new cases, its expected there will be a large number of recoveries 10 days later. 

![Resolved cases over time](https://github.com/BilalQadar/Covid19Canada/blob/master/figures/pandemic%20visualization/resolved.png)

The number of active cases is the total number of unresolved cases in Canada at any given time. This is a figure which provides an indication of where in the pandemic cycle Canada currently is.

![Active cases over time](https://github.com/BilalQadar/Covid19Canada/blob/master/figures/pandemic%20visualization/active.png)

All the figures above are based on real data. The next section will manipulate that data and make predictions. As mentioned in the disclaimer all figures below **do not** accurately project infections. 

The model used to predict future infections is based on the SIR (suseptible, infected and recovered) model. This model splits the total population (N) into a suseptible, infected and recovered population. The model assumes that the population remains fixed (the birth rate and death rate are equivalent). Another assumption made is once a persons case is marked resolved they can't become infected again. 

![Suseptible Population](https://www.codecogs.com/eqnedit.php?latex=S_{t&plus;1}&space;=&space;\frac{\beta}{N}I_tS_t&space;&plus;&space;b(I_t&space;&plus;&space;R_t)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?S_{t&plus;1}&space;=&space;\frac{\beta}{N}I_tS_t&space;&plus;&space;b(I_t&space;&plus;&space;R_t)" title="S_{t+1} = \frac{\beta}{N}I_tS_t + b(I_t + R_t))

![Infected Population](https://latex.codecogs.com/gif.latex?I_{t&plus;1}&space;=&space;I_t(1-\gamma&space;-b)&space;&plus;&space;\frac{\beta}{N}I_tS_t" title="I_{t+1} = I_t(1-\gamma -b) + \frac{\beta}{N}I_tS_t)

![Recovered Population](https://www.codecogs.com/eqnedit.php?latex=R_{t&plus;1}&space;=&space;R_t(1-b)&space;&plus;&space;\gamma&space;I_t" target="_blank"><img src="https://latex.codecogs.com/gif.latex?R_{t&plus;1}&space;=&space;R_t(1-b)&space;&plus;&space;\gamma&space;I_t" title="R_{t+1} = R_t(1-b) + \gamma I_t)

# Citation
COVID-19 Canada Open Data Working Group. Epidemiological Data from the COVID-19 Outbreak in Canada. https://github.com/ishaberry/Covid19Canada. (Access Date). 

# Accurate as of: 
April 4th, 2020
