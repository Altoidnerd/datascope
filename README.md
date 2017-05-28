# datascope
Datascope challenge questions
(Allen Majewski - 2017)

## 1. Which stop has the highest average ridership per day, and what is it?

    > cd warmups
    > python3 highest_mean.py
    The station with the highest mean ridership is station 40380
    The mean ridership there in riders/day is 13662.780496150555
    

## 2. Which stop has the greatest standard deviation in weekday (exclude holidays) ridership per day, and what is it?

    > python3 highest_weekday_stddev.py
    The station with the highest weekday standard deviation in ridership is station 41660
    The standard deviation there in riders/day is 4302.097081764574
    The mean ridership there in riders/day is 15745.73891746265     


## 3. Imagine you're a business owner in Chicago looking to open a new location. Any kind of business will do. In the form of writing, potentially supplemented by sketches (computer-drawn or hand-drawn) and links, we want to see your response to these questions: 

*        What questions could you potentially explore/answer with this data?

First of all, "where should I open my business" or "is location X a good location for me?"  To answer this, I could look at the standard deviations as suggested in the warmups.  If my business is one that can deal with large fluctuations, then having a large standard deviation isn't a problem.  If on the other hand my business is one that cannot really deal with "getting slammed" occasionally, I should pick a location where the mean is high and the standard deviation is lower.

Secondly, when are the big fluctuations in the ridership, what are the periodicities, and what causes those fluctuations?  It would be nice to be prepared for those fluctuations; we can see in the data for stop 40380 there is clearly an annual dip in riders. What other fine grained periodicities are there?  Are fridays much busier than mondays?  There are lots of questions that could be asked in regards to periodicity that could help a business prepare its schedules and staffing.


![40380 image]('https://github.com/Altoidnerd/datascope/blob/master/img/40380.png')
Clear annual dips

![40380 weekdays]('https://github.com/Altoidnerd/datascope/blob/master/img/40380_weekday.png')
There is a lot more detail apparent in the weekday only plots. What is the reason for the number of low outliers that appear to have annual recurrence? 


*        Ideally, what other data would you gather or combine to learn even more?

If I wanted to account for what is causing the outliers, I'd need to test a hypothesis against some other data, like for example, a sports schedule.  Nobody likes the White Sox, but does the ridership spike on days with a Cubs game?  How about lollapalooza? Do the annual artifacts correspond with various seasonal data?  Is there a correlation with temperature data? Once you think of the right question to ask, the data needed to test the hypothesis is more clear.

*        How would you want to see data presented, to make it actionable by you or others?

Plots. Anything but tables of numbers.

I like scatter plots.  Clever visualization is always important when trying to make a case.  The right kind of visualization is much more convincing to non-experts than just a scatter plot.



