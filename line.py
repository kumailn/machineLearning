import numpy
import matplotlib.pyplot as plt
def slope(l):
    # Takes in list of x, y pairs, finds exact slope of best line of scatter plot
    xs, ys = [], []
    for i in range(len(l)):
        xs += [l[i][0]]
        ys += [l[i][1]]
    mx, my = mean(xs), mean(ys)
    return ((mx*my) - (mean(mul(xs, ys))))/((mean(xs)**2) - (mean(sql(xs))))

def intercept(l):
    xs, ys = [], []
    for i in range(len(l)):
        xs += [l[i][0]]
        ys += [l[i][1]]
    mx, my = mean(xs), mean(ys)
    return(my - slope(l)*mx)

def mean(l):
    m = 0
    for i in l:
        m += i
    return m/len(l)

def mul(l, l2):
    ll = []
    for i in range(len(l)):
        ll += [l[i] * l2[i]]
    return (ll)

def sql(l):
    ll = []
    for i in l:
        ll += [i ** 2]
    return ll

def xs(l):
    xs2, ys = [], []
    for i in range(len(l)):
        xs2 += [l[i][0]]
    return xs2
def ys(l):
    xs, ys2 = [], []
    for i in range(len(l)):
        ys2 += [l[i][1]]
    return ys2

def lineOfRegression(l):
    ll = []
    for i in xs(l):
        ll += [(slope(l) * i + intercept(l))]
    return ll

coordinates = [[2,7],[5,13], [20, 43]]

print(slope([[2,7],[5,13], [20, 43]]))
print(intercept([[2,7],[5,13], [20, 43]]))
print(xs([[2,7],[5,13], [20, 43]]))
print(mean([1,2,3]))
print(lineOfRegression([[2,7],[5,13], [20, 43]]))
plt.scatter (xs([[2,7],[5,13], [20, 43]]), ys(([[2,7],[5,13], [20, 43]])))
print(lineOfRegression(coordinates))
plt.show()
