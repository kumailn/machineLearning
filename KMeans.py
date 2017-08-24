import random
import pandas
import matplotlib.pyplot as pyplot
from matplotlib import style
style.use("ggplot")
import numpy
from sklearn.cluster import KMeans


dataFrame = pandas.read_excel("""C:\\Users\\Ali\\Dropbox\\Python\\machineLearning\\Data\\titanic.xls""")
dataFrame.drop(["body", "name"], 1, inplace=True)
dataFrame.convert_objects(convert_numeric=True)
dataFrame.fillna(0, inplace=True)
print(dataFrame.head())



G = numpy.array([[1,2],[3,4]])
for i in range(15):
    y = random.randint(1,40)
    u = random.randint(1,40)
    H = numpy.array([[y, u]])
    G = numpy.concatenate((H, G))

for i in range(15):
    y = random.randint(50,111)
    u = random.randint(50,111)
    H = numpy.array([[y, u]])
    G = numpy.concatenate((H, G))

classifier = KMeans(n_clusters=2)
classifier.fit(G)

centroids = classifier.cluster_centers_
labels = classifier.labels_


X = numpy.array([[1,1], [2,4], [3,5], [2,1], [14,22], [21,12], [17,115], [12,26], [22,11]])
print(G)

#s = Size of
pyplot.scatter(G[:, 0],G[:, 1], s=50,  linewidths = 5, zorder = 10)
pyplot.scatter(centroids[:,0], centroids[:,1], marker="x", s=100, linewidths=5, zorder=10)
pyplot.show()