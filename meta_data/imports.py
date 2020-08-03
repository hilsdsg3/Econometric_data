import pandas as pd  # for DataFrames, dataframe for time series data
import pandas_ta as ta  # !pip install pandas_ta
import numpy as np  # array,matrix,random numbers
import math
import sys
import yfinance as yf  # !pip install yfinance
from io import StringIO  # before pandas_datareader
from pandas_datareader import data as pdr
from pandas_datareader import data, wb
from pandas import ExcelWriter
from pandas import ExcelFile
from pandas.plotting import register_matplotlib_converters
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.dates as mdates
from matplotlib import rc, interactive
import datetime as dt
from datetime import timedelta, datetime, date, time
import time
import pathlib
from pathlib import Path  # to read/write files
import os
from os import path
import ast
import re
import requests  # scraping the web
from urllib.request import urlopen
from IPython.core.interactiveshell import InteractiveShell
from IPython.display import display
import fredapi
from fredapi import Fred
#import global_vars_and_constants

InteractiveShell.ast_node_interactivity = "all"
register_matplotlib_converters()
pd.core.common.is_list_like = pd.api.types.is_list_like