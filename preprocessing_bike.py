from collections import Counter
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
import pandas as pd
from pandas.tseries.holiday import USFederalHolidayCalendar as calendar
from datetime import date, datetime

"""

"""
class Preprocess_bike:
   
    def __init__(self):
        pass
        
    
    def fit(self, X, y=None):
        return self
    
    #function to get season based on date
    def get_season(self, now):
        Y = 2000 # dummy leap year to allow input X-02-29 (leap day)
        seasons = [('winter', (date(Y,  1,  1),  date(Y,  3, 20))),
                ('spring', (date(Y,  3, 21),  date(Y,  6, 20))),
                ('summer', (date(Y,  6, 21),  date(Y,  9, 22))),
                ('autumn', (date(Y,  9, 23),  date(Y, 12, 20))),
                ('winter', (date(Y, 12, 21),  date(Y, 12, 31)))]
        now = now.replace(year=Y)
        return next(season for season, (start, end) in seasons
                    if start <= now <= end)
    
    #implement get if date is holiday, convert date format, merge holiday column, get season and encode all
    def transform(self, X, y=None):
        
        #import holiday calendar
        cal = calendar()
        holidays = cal.holidays(start='2019-01-01', end='2019-12-31')#.to_pydatetime()
        holidays = pd.DataFrame(holidays)
        holidays = holidays.rename(columns={0: 'holidays'})
        
        #convert date format
        X['Day_of_Date'] = pd.to_datetime(X['Day_of_Date'])
        X['Day_of_Week'] = X['Day_of_Date'].dt.dayofweek
        X['Day_of_Year'] = X['Day_of_Date'].dt.dayofyear
        
        #convert trip ID string to int
        X['Count of Trip Id'] = X['Count of Trip Id'].str.replace(',', '').astype(int)
        
        X = pd.merge(X, holidays, left_on='Day_of_Date', right_on ='holidays', how = 'left')
        #X = X.rename(columns={'Day_of_Date': 'Day_of_Date'})
        
        
        #season
        X['season'] = X.Day_of_Date.map(self.get_season)

        #Encode season    
        X.loc[X['season'] == 'winter', 'winter'] = 1
        X.loc[X['season'] == 'spring', 'spring'] = 1
        X.loc[X['season'] == 'summer', 'summer'] = 1
        X.loc[X['season'] == 'autumn', 'autumn'] = 1

        X['winter'] = X['winter'].fillna(0)
        X['spring'] = X['spring'].fillna(0)
        X['summer'] = X['summer'].fillna(0)
        X['autumn'] = X['autumn'].fillna(0)

        #Fill holiday NaT with 0
        X['holidays'] = X['holidays'].fillna(0)

        #Create column for 0 non-holiday and 1 holiday
        X.loc[X['holidays'] == 0, 'holiday'] = 0
        X['holiday'] = X['holiday'].fillna(1)


        X.drop(["holidays", "season"], axis = 1, inplace = True)
        
        
        
        return X
    
    def fit_transform(self,X, y=None):
        self.fit(X,y)
        return self.transform(X, y) 

    
