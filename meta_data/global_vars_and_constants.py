import sys
import pandas as pd
from datetime import timedelta, datetime, date, time
import API

# if __name__ == '__main__':
#     main(sys.argv[1])

#  Global constants
DATA_TYPE = 'Adj Close'
DAYS_LOOK_BACK = 5110  # 12*252 years expresed in days
HOW_RECENT = 0
MAIN_FOLDER = 'C:/Users/champ/Python_proj/base_financial_repo/'
ECONO_DATA_REPO = 'Econometric_data_repo/'
META_FILE_FOLDER = 'meta_data/'
GIT_IGNORE = 'C:/Users/champ/Python_proj/git_ignore/'
SECURITIES_FILE = 'Securities research.csv'
HOLIDAYS_FILE = 'Federal_holidays.csv'
SECURITY_ARRAY = ['sectors','inx']
FRED_API = FRED_API_KEY # Your API goes here
FIGURE_WIDTH = 12
FIGURE_HEIGHT = 6
LINE_WIDTH = 2
GRAPH_FONT_SIZE = 12
INX = 'spy'


#  Global variables
#end_date = pd.Timestamp('today')
end_date = pd.to_datetime('today')
#end_date = pd.to_datetime('now').tz_localize("GMT").tz_convert('America/Los_Angeles')
end_date = end_date.replace(hour=0, minute=0, second=0, microsecond=0)
start_date = end_date - timedelta(days=DAYS_LOOK_BACK)
fred = Fred(FRED_API)

META_FILE_FOLDER_LOCATION =  MAIN_FOLDER + ECONO_DATA_REPO + META_FILE_FOLDER
securities_file_location = META_FILE_FOLDER_LOCATION + SECURITIES_FILE
Securities_file_import_from_csv = pd.read_csv(securities_file_location, sep=';')
    
Holidays = pd.read_csv(MAIN_FOLDER + ECONO_DATA_REPO + META_FILE_FOLDER +
                       HOLIDAYS_FILE, sep=',', index_col='Date')
Holidays.index = pd.to_datetime(Holidays.index, format='%m/%d/%Y')
Today = pd.Timestamp('today').normalize()
#kw_save = dict(bbox_iches='tight', transparent=True)

econ_data_labels = { "LEI":
      { "column_name": "USSLIND",
        "color": "gray",
        "name": "LEI",
        "text": "Leading Economic Indicator"
      },"MORT30YR": 
      { "column_name": "MORTGAGE30US",
        "color": "red",
        "name": "30yr Mort",
        "text": "0-yr Mortgage rate"
      },"Unemployment": 
      { "column_name": "ICSA",
        "color": "blue",
        "name": "Unem",
        "text": "Unemployent"
      }}
econ_data_titles = { 'titles':
      { 'chart_title': 'Econometric Chart - General Indicators',
        'y_axis_title': 'Annual percentage',
        'x_axis_title': 'Date',
      }}

econ_data_titles2 = { 'titles':
      { 'chart_title': 'Econometric Chart - FRED Rates',
        'y_axis_title': 'Annual percentage',
        'x_axis_title': 'Date',
      }}


econ_data_labels2 = { "Risk-free rate":
      { "column_name": "DTB3",
        "color": "gray",
        "name": "RF-3moTBill",
        "text": "Risk-free"
      },"Core-CPI": 
      { "column_name": "CPILFESL",
        "color": "red",
        "name": "Core-CPI",
        "text": 'Core-CPI'
      },"10y-2yR": 
      { "column_name": "T10Y2Y",
        "color": "blue",
        "name": "10-2 Yield",
        "text": "10-2 Yield"
      }}

print("Ready to go !")