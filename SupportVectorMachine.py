#svm v21
import numpy
from sklearn import preprocessing, cross_validation, neighbors, svm
import  pandas

def svm():
    dataFrame = pandas.read_csv("""C:\\Users\\Ali\\Dropbox\\Python\\machineLearning\\Data\\cancer-wisconsin.data.txt""")
    dataFrame.replace("?", -99999, inplace=True)
    dataFrame.drop(["id"], 1, inplace=True)
    print(dataFrame.head())

    y = numpy.array(dataFrame["class"])
    X = numpy.array(dataFrame.drop(["class"], 1))

    X_train, X_test, Y_train, Y_test = cross_validation.train_test_split(X, y, test_size=0.2)

    classifier = svm.SVC()
    classifier.fit(X_train, Y_train)
    accuracy = classifier.score(X_test, Y_test)
    print(accuracy)

    example_test = numpy.array([4,2,1,1,1,2,3,2,1])

    pred = classifier.predict(example_test)
    print(pred)

svm()