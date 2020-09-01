## Sector, Index, and Econometric Overview
A current look at how the 11 different US market sectors are performing with regards to relative strength and dividend chart. Also a graphical look at the S&P's bollinger bands, 50 day MA , and 200 day MA. Followed by two econometric graphs displaying select FRED rates like risk-free rate, unemployment data, 30-yr mortgage rate, leading economic indicator, Core CPI, 10-2mo yield rate. My [github.io](https://hilsdsg3.github.io/hildsg3/) site shows the graphs in interactive Plotly graphs. I like these graphs because you can zoom and narrow in on a certain timeframe.   


<p align="center"><img width=60% src="https://github.com/hilsdsg3/Econometric_data/blob/master/meta_data/media/Bull_bear.jpg"></p>

<br>

### Sector Relative Strength
The information on the following asecending chart is the mean returm for 1,3,6,12 month, dividend information, and the regular volume of the ETF. Highlighted is the Healthcare ETF XLV with a mean return of 11.5% with a dividend yeild 2.27% and a effective dividend rate (dividend minus expense) of 2.4%. Also I have the past dividend timestamp or more commonly called EX_dividend date. The future approxiamate dividend date and the days left for the dividend payout.       
<p align="center"><img width=80% src="https://github.com/hilsdsg3/Econometric_data/blob/master/meta_data/media/sector_chart.png"></p>

### S&P Market chart
On the chart is the 200 and 50 day MA as well the bollinger bands. One could use these daily charts for a simply strategy as the Golden-Death cross. A bullish sign for the S&P occurs when the 50-day moving average (MA 50 - blue line) rises above the 200-day (MA 200 - purple line). This event is called the Golden Cross.
Conversely, the Death cross event occurs when the 50-day MA decreases below the 200-day MA and would be considered bearish. Genrally, a bullish sign are prices that rise and bearish sign would be a decrease in prices.    
<p align="center"><img width=80% src="https://github.com/hilsdsg3/Econometric_data/blob/master/meta_data/media/Golden_Death_cross.jpg"></p>

<br>

# Pre-requisites :
1. Install [Python 3.8+](https://www.python.org/downloads/source/)
2. To install Jupyter-Lab or Jupyter-Notebook, you do NOT have to install Anaconda. If don't want as comprehensive software as Anaconda then install [jupyterlab or jupyternotebook](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html) here. Also there are brief instructions of how to install virtual environments which are a good idea.   
3. Clone the project from : git clone https://github.com/hilsdsg3/Econometric_data.git
4. Install a the ![dependency python packages here] (https://github.com/hilsdsg3/Econometric_data/blob/master/requirements.txt) from this cloned file
with "python -m pip install -r requirements.txt" in the cmd line. Your particular system may vary how you can install packages.  
5. Next you will need an FRED API. Create a [US Federal Reserve Economic Data (FRED) user name here](https://research.stlouisfed.org/useraccount/login/secure/).
6. Then log-in to create a [FRED API here](https://research.stlouisfed.org/docs/api/api_key.html)

## Display improvements - pending features
1. Use an algorithm to detect a golden vs a death cross in the market chart  

## Latest Development Changes
```bash
git clone https://github.com/hilsdsg3/Econometric_data.git
```

## Disclaimer
My content is intended to be used and must be used for informational purposes only. It is important to do your own analysis before making any investment based on your own personal circumstances. You should seek independent financial advice from a professional in connection with, or independently research and verify, any information that you find on this page, whether for the purpose of making an investment decision or otherwise.


## Contributing
Please take a look at my [contributing](https://github.com/hilsdsg3/Econometric_data/blob/master/CONTRIBUTING.md) guidelines if you're interested in helping!


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)
[![GitHub Issues](https://img.shields.io/github/issues/hilsdsg3/Econometric_data.svg)](https://github.com/hilsdsg3/Econometric_data/issues)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)


