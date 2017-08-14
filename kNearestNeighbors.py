##
import numpy
from sklearn import preprocessing, cross_validation, neighbors
import  pandas

def n():
    dataFrame = pandas.read_csv("""C:\\Users\\Ali\\Dropbox\\Python\\machineLearning\\Data\\cancer-wisconsin.data.txt""")
    dataFrame.replace("?", -99999, inplace=True)
    dataFrame.drop(["id"], 1, inplace=True)
    print(dataFrame.head())

    y = numpy.array(dataFrame["class"])
    X = numpy.array(dataFrame.drop(["class"], 1))

    X_train, X_test, Y_train, Y_test = cross_validation.train_test_split(X, y, test_size=0.2)

    classifier = neighbors.KNeighborsClassifier()
    classifier.fit(X_train, Y_train)
    accuracy = classifier.score(X_test, Y_test)
    print(accuracy)

    example_test = numpy.array([4,2,1,1,1,2,3,2,1])

    pred = classifier.predict(example_test)
    print(pred)



def car():
    dataFrame = pandas.read_csv("""C:\\Users\\Ali\\Dropbox\\Python\\machineLearning\\Data\\car.data.txt""")
    dataFrame.replace("low", 1, inplace=True)
    dataFrame.replace("med", 2, inplace=True)
    dataFrame.replace("high", 3, inplace=True)
    dataFrame.replace("vhigh", 4, inplace=True)
    dataFrame.replace("5more", 5, inplace=True)
    dataFrame.replace("small", 1, inplace=True)
    dataFrame.replace("big", 3, inplace=True)
    dataFrame.replace("more", 5, inplace=True)






    #dataFrame.drop(["id"], 1, inplace=True)
    print(dataFrame.tail())
    d2 = dataFrame["accept"]
    d2.replace("vgood", "acc", inplace=True)
    d2.replace("good", "acc", inplace=True)
    y = numpy.array(d2)
    X = numpy.array(dataFrame.drop(["accept"], 1))

    X_train, X_test, Y_train, Y_test = cross_validation.train_test_split(X, y, test_size=0.2)

    classifier = neighbors.KNeighborsClassifier()
    classifier.fit(X_train, Y_train)
    accuracy = classifier.score(X_test, Y_test)
    print(accuracy)

    example_test = numpy.array([2, 1, 4, 4, 2, 3])

    pred = classifier.predict(example_test)
    print(pred)


car()