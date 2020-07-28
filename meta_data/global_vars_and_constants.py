#  Global constants
DATA_TYPE = 'Adj Close'
DAYS_LOOK_BACK = 4500  # 12*252 years expresed in days
HOW_RECENT = 0
MAIN_FOLDER = 'C:/Users/champ/Python_proj/base_financial_repo/'
META_FILE_FOLDER = 'meta_data/'
SECURITIES_FILE = 'Securities research.csv'
HOLIDAYS_FILE = 'Federal_holidays.csv'


#  Global variables
end_date = pd.Timestamp('today')
end_date = end_date.replace(hour=0, minute=0, second=0, microsecond=0)
start_date = end_date - timedelta(days=DAYS_LOOK_BACK)
fred = Fred(FRED_API)
Securities_file_location = MAIN_FOLDER + META_FILE_FOLDER + SECURITIES_FILE
Holidays = pd.read_csv(MAIN_FOLDER + META_FILE_FOLDER +
                       HOLIDAYS_FILE, sep=',', index_col='Date')
Holidays.index = pd.to_datetime(Holidays.index, format='%m/%d/%Y')
Today = pd.Timestamp('today').normalize()
kw_save = dict(bbox_iches='tight', transparent=True)

