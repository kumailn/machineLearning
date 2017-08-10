import pandas as panda
import quandl

ticker = "WIKI/TSLA"

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

print(dataFrame2.tail())
print(dataFrame2.head())
#print(dataFrame["differencePercent"].tail())
#print(dataFrame["dayPercentChange"].tail())