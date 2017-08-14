import math


def euclidean_distance(c):
    # Takes in two coordinates in n dimensions and returns the distance between them
    l = []
    q, p = 0, 0
    if len(c) > 1:
        for i in range(len(c[0])) :
            q = (c[0][i] - c[1][i]) ** 2
            l += [q]
    x = sum(l)
    return math.sqrt(x)


print(euclidean_distance([[1,2,3],[10,23,31]]))