#v19
import math
import numpy
import matplotlib.pyplot
import warnings
from matplotlib import style
from collections import Counter
import pandas
import random

sample_dataset = {"k":[[1,2],[2,3],[3,1]], "r":[[6,5], [7,7], [8,6]]}
sample_point = [5,7]


def euclidean_distance(c):
    # Takes in two coordinates in n dimensions and returns the distance between them
    l = []
    q, p = 0, 0
    for i in range(len(c[0])) :
        q = (c[0][i] - c[1][i]) ** 2
        l += [q]
    x = sum(l)
    return math.sqrt(x)

def k_nearest_neighbors(dataset, predict, k=3):
    if len(dataset) >= k:
        warnings.warn("K is less than total groups")
    all_distances = []
    for group in dataset:
        for features in dataset[group]:
            euclid_dist = numpy.linalg.norm(numpy.array(features) - numpy.array(predict))
            all_distances.append([euclid_dist, group])

    vote = [i[1] for i in sorted(all_distances)[:k]]
    vote_result = Counter(vote).most_common(1)[0][0]
    return vote_result

# result = k_nearest_neighbors(sample_dataset, sample_point, k=3)
# print(result)

# for i in sample_dataset:
#     for j in sample_dataset[i]:
#         print(j)
#         matplotlib.pyplot.scatter(j[0], j[1], s=100, color=i)
# matplotlib.pyplot.show()
#print(euclidean_distance([[1,2,3],[10,23,31]]))

dataFrame = pandas.read_csv("""C:\\Users\\Ali\\Dropbox\\Python\\machineLearning\\Data\\cancer-wisconsin.data.txt""")
dataFrame.replace("?", -99999, inplace=True)
dataFrame.drop(["id"], 1, inplace=True)
all_data = dataFrame.astype(float).values.tolist()

random.shuffle(all_data)

test_size = 0.2
train_set = {2:[], 4:[]}
test_set = {2:[], 4:[]}

train_data = all_data[:-int(test_size * len(all_data))]
test_data = all_data[-int(test_size * len(all_data)):]

for i in train_data:
    train_set[i[-1]].append(i[:-1])
for i in test_data:
    test_set[i[-1]].append(i[:-1])

correct = 0
total = 0

for group in test_set:
    for data in test_set[group]:
        vote = k_nearest_neighbors(train_set, data, k=5)
        if group == vote:
            correct += 1
        total += 1

print("Accuracy: ", correct/total)
