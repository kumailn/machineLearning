import math
import pandas as panda
import quandl
import numpy
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression

ticker = "WIKI/TSLA"

forecastColumn = "Adj. Close"

dataFrame = quandl.get(ticker)
dataFrame = dataFrame[["Adj. Open", "Adj. High", "Adj. Low", "Adj. Close", "Adj. Volume"]]
# Calculates the difference in percent between days high and low price (ie Volatility)
dataFrame["differencePercent"] = (dataFrame["Adj. High"] - dataFrame["Adj. Low"]) / dataFrame["Adj. Close"] * 100
# Calculates the percent change in stock price for that day
dataFrame["dayPercentChange"] = (dataFrame["Adj. Close"] - dataFrame["Adj. Open"]) / dataFrame["Adj. Open"] * 100

dataFrame = dataFrame[["Adj. Close", "differencePercent", "dayPercentChange", "Adj. Volume"]]

dataFrame2 = dataFrame[["Adj. Close", "differencePercent", "dayPercentChange", "Adj. Volume"]]
# Dataframe2 stores Adjusted Volume in Millions
dataFrame2["Adj. Volume"] = dataFrame["Adj. Volume"] / 1000000

# Fill N/A data with extreme values to create outliers
dataFrame.fillna(-99999, inplace=True)
dataFrame2.fillna(-99999, inplace=True)

# Gets length of 1% of dataFrame
dataFrameLength = len(dataFrame)
forecastLength = int(math.ceil(0.01*dataFrameLength))
dataFrame["label"] = dataFrame[forecastColumn].shift(-forecastLength)

# Features
X = numpy.array(dataFrame.drop(["label"], 1))

# Labels
y = numpy.array(dataFrame["label"])

X = preprocessing.scale(X)
X = X[:-forecastLength + 1]
dataFrame.dropna(inplace=True)
y= numpy.array(dataFrame["label"])

print(len(X), len(y))

print(forecastLength, dataFrameLength)
print(dataFrame.tail())
print(dataFrame.head())
#print(dataFrame["differencePercent"].tail())
#print(dataFrame["dayPercentChange"].tail())