import pandas
import matplotlib.pyplot as pyplot
from matplotlib import style
style.use("ggplot")
import numpy
from sklearn.cluster import KMeans


dataFrame = pandas.read_excel("""C:\\Users\\Ali\\Dropbox\\Python\\machineLearning\\Data\\titanic.xls""")
print(dataFrame.head())