import pandas as panda
import quandl

dataFrame = quandl.get("WIKI/TSLA")
dataFrame = dataFrame[["Adj. Open", "Adj. High", "Adj. Low", "Adj. Close", "Adj. Volume"]]
# Calculates the difference in percent between days high and low price (ie Volatility)
dataFrame["differencePercent"] = (dataFrame["Adj. High"] - dataFrame["Adj. Low"]) / dataFrame["Adj. Close"] * 100

print(dataFrame.tail())
print(dataFrame["differencePercent"].tail())