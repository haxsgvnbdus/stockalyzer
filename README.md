# stockalyzer


**Team Members**

Han Ngo | Yi Man

**Project Goals**

- To apply deep learning techniques (Recurrent Neural Network algorithm) to predict the future stock closing value of a given stock across a given period of time. Using **Long Short Term Memory network** improved training accuracy and avoided overfitting issue.

- To build financial analysis for a user-specified group of stocks based on daily returns by sampling and calculating volatility of a given stock over a specific time frame.

**Questions Sought To Answer**

1. Given a set of symbols (company indexes), how would the model predict stock price change in a specified time frame?
2. How efficient does the neural network work towards different sets of data? Does it cause too much over-fitting or under-fitting?
3. What would be a good decision in different situations, e.g. if we decided to previously buy the stock and there is an increase in the stock price?
4. Once decision is made, based on historical data source, how does the program generate analysis for us to see if the action yields any profits?

**Application of Knowledge**

Investment firms, hedge funds, and daily stock traders can:
- Predict stock prices with machine learning model in a specific time frame
- Project financial analysis and comparison within a specified set of stocks based on historical datasets
- Better decide which stock may have less risk when examining the stock&#39;s volatility in the overall market

**Tools/Libraries**
- Quandl
- Tensorflow/Keras
- MatplotLib
- Numpy
- Pandas
- Sklearn
- Python 2.7

**Preparation Work**
- Data Collection &amp; Cleaning
- Data Normalization
- Data Transformation
- Data Integration
- Model Construction

**Data source**
- SP500 Index
https://raw.githubusercontent.com/datasets/s-and-p-500-companies/master/data/constituents-financials.csv/

- Stock Historical Data
https://finance.yahoo.com/quote/%5EGSPC/history?p=%5EGSPC/

**Video Demonstration:** https://github.com/haxsgvnbdus/stockalyzer/blob/master/Team27\_Stockalyzer\_Part6.pdf

**Final Project** Paper:https://github.com/haxsgvnbdus/stockalyzer/blob/master/Team27\_Stockalyzer\_Part4.pdf
