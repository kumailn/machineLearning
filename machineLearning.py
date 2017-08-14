import math, datetime
import pandas as panda
import quandl
import numpy
import re
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style



style.use("ggplot")
ticker = "WIKI/GOOGL"

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
X = preprocessing.scale(X)
X_now = X[-forecastLength:]
X = X[:-forecastLength]


# Labels
dataFrame.dropna(inplace=True)
y = numpy.array(dataFrame["label"])
y= numpy.array(dataFrame["label"])

#dataFrame.dropna(inplace=True)
#dataFrame.fillna(355, inplace=True)

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)

# Set machine learning algorithm
classifier = LinearRegression(n_jobs=-1)
#classifier = svm.SVR()


classifier.fit(X_train, y_train)
accuracy = classifier.score(X_test, y_test)

forecastSet = classifier.predict(X_now)

print(len(X), len(y))
print(accuracy)
print(forecastLength, dataFrameLength)
print(dataFrame.tail())
print(dataFrame.head())
print(forecastSet)

dataFrame["Forecast"] = numpy.nan
last_day = dataFrame.iloc[-1].name
last_unix = last_day.timestamp()
one_day = 86400
next_unix = last_unix + one_day


for i in forecastSet:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    dataFrame.loc[next_date] = [numpy.nan for _ in range(len(dataFrame.columns)-1)] + [i]

dataFrame["Adj. Close"].plot()
dataFrame["Forecast"].plot()
plt.legend(loc=4)
plt.xlabel("Date")
plt.ylabel("$")
plt.title(re.sub("WIKI/", "", ticker))
plt.show()