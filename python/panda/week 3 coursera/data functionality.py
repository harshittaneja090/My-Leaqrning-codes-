import pandas as pd
import numpy as np
#time stamp 
print("pd.Timestamp('4/jun/2020 10:05AM') :",pd.Timestamp('4/jun/2020 10:05AM'))
#time  output  2020-06-04 10:05:00
##Period
print("pd.Period('1/2016'):",pd.Period('1/2016'))
print("pd.Period('3/5/2016') :",pd.Period('3/5/2016'))
#DatetimeIndex
#here we are creating series with data timestamps and index as list
#t1= pd.Series(         data                                                                        ,index           )
t1 = pd.Series([pd.Timestamp('2016-09-01'), pd.Timestamp('2016-09-02'), pd.Timestamp('2016-09-03')],index=list('abc'))
print("t1")
print(t1)
#here data is timestamp and index is a list type we can also interchange them 
print("type(t1) :",type(t1))
print("type(t1.index) :",type(t1.index))
#t0=pd.series(data      ,          index                                                                     )
t0=pd.Series(list('abc'),[pd.Timestamp('2016-09-01'), pd.Timestamp('2016-09-02'), pd.Timestamp('2016-09-03')])
print("t0\n")
print(t0)
print("type(t0) :",type(t0))
print("type(t0.index) :",type(t0.index))


#PeriodIndex
#t2=pd.Series(  data       ,                                      index                       )
t2 = pd.Series(list('def'), [pd.Period('2016-09'), pd.Period('2016-10'), pd.Period('2016-11')])
print(t2)
print("type(t2.index) :",type(t2.index))
#list of dates
d1 = ['2 June 2013', 'Aug 29, 2014', '2015-06-26', '7/12/16']
#ts3=pd.DataFrame(np.random.randint(10 to100, (r0w,column)), index=d1(list of dates), columns=['a','b']))
ts3 = pd.DataFrame(np.random.randint(10, 100, (4,2)), index=d1, columns=list('ab'))
print(ts3)
#using date time we put pandas date times in specific format
ts3.index = pd.to_datetime(ts3.index)
print(ts3)
print("'4.7.12', dayfirst=True) :",pd.to_datetime('4.7.12', dayfirst=True))
# time delta
#In this we are printing the time gap of 1 september and 3 september this is will two days 
print(pd.Timestamp('9/3/2016')-pd.Timestamp('9/1/2016'))
#we are adding 12 days and 3 houres in 2 september
#this will become 2+12=14 days or 14 september and time will be 11:10 pm at 14 september 
print(pd.Timestamp('9/2/2016 8:10AM') + pd.Timedelta('12D 3H'))

#Working with Dates in a Dataframe
'''
this  dates will print 9 dates as period is 9 with gap of 2 weeks as frequency is 2w
so first it will print 2 oct(10) 2016 ,16 oct(10) 2016, 30 oct(10) 2016 ,13 nov(11) 2016 and so on  
'''
dates = pd.date_range('10-01-2016', periods=9, freq='2W-SUN')
print(dates)
#creating a dtaframe and colums are  count 1 and count 2 with any random values and index is set as dates 
df = pd.DataFrame({'Count 1': 100 + np.random.randint(-5, 10, 9).cumsum(),
                  'Count 2': 120 + np.random.randint(-5, 10, 9)}, index=dates)
print(df)
'''
output is as follows for understanding 
         Count 1  Count 2
2016-10-02       97      122
2016-10-16       97      116
2016-10-30       93      124
2016-11-13       99      117
2016-11-27       99      125
2016-12-11      104      123
2016-12-25      100      117
2017-01-08       99      122
2017-01-22       94      129
'''
# we can also check that these dates in data frame is which day of week 
#print('df.index.weekday_name :',df.index.weekday_name)
print("df.diff() :")
#this will print date gapes between each days
print(df.diff())
print("df.resample('M').mean() :")
print(df.resample('M').mean())
print("df['2017'] particular year")
print(df['2017'])
print("df['2016-12'] particular month")
print(df['2016-12'])
print(df.asfreq('W', method='ffill'))
