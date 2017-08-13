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
    # Determines the intercept of the line of best fit for a list of given x, y pairs
    xs, ys = [], []
    for i in range(len(l)):
        xs += [l[i][0]]
        ys += [l[i][1]]
    mx, my = mean(xs), mean(ys)
    return(my - slope(l)*mx)

def mean(l):
    # Finds mean of a list
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
    # Extracts x points from a list of x,y pairs
    xs2, ys = [], []
    for i in range(len(l)):
        xs2 += [l[i][0]]
    return xs2

def ys(l):
    # Extracts y points from a list of x,y pairs
    xs, ys2 = [], []
    for i in range(len(l)):
        ys2 += [l[i][1]]
    return ys2

def line_of_regression(l):
    # Determines the y values for the line of best fit
    ll = []
    for i in xs(l):
        ll += [(slope(l) * i + intercept(l))]
    return ll

def squared_error(old_ys, ys_line):
    # Determines the squared error for a list of raw y points and a list of y points for the line of best fit
    old_ys = numpy.array(old_ys)
    line_ys = numpy.array(ys_line)
    return sum((line_ys - old_ys) ** 2)

def coefficient_of_determination(l):
    # Calculates the coefficient of determination for a given list of x,y pairs
    y_mean_line = [mean(ys(l)) for y in ys(l)]
    regression_squared_error = squared_error(ys(l), line_of_regression(l))
    y_mean_squared_error = squared_error(ys(l), y_mean_line)
    return(1 - (regression_squared_error/y_mean_squared_error))

coordinates = [[2,7],[5,13], [20, 43], [-2, 213]]

print(slope(coordinates))
print(intercept(coordinates))
print(xs(coordinates))
print(line_of_regression(coordinates))
plt.scatter (xs(coordinates), ys((coordinates)))
plt.plot(xs(coordinates), line_of_regression(coordinates))
print(line_of_regression(coordinates))

print("The coefficient of determination is %" + (str(coefficient_of_determination(coordinates) * 100)))
plt.show()
