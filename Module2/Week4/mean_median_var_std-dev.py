
### Question 1
import numpy as np

def compute_mean(x):
  return np.sum(x) / len(x)

x = [2, 0, 2, 2, 7, 4, -2, 5, -1, -1]

print("The number of elements: ", len(x))
print("The sum of elements: ", np.sum(x))
print("Mean : ", compute_mean(x))

### Question 2

def compute_median(x):
  size = len(x)
  print("Size: ", size)
  x = np.sort(x)
  print("x.sort: ", x)
  if (size % 2 == 0):
    return (1/2*(x[int(size/2)-1] + (x[int(size/2) + 1 - 1])))
  else:
    return x[int((size+1)/2)-1]

x = [1, 5, 4, 4, 9, 13]
print("Median: ", compute_median(x))

### Question 3

def compute_std(x):
  mean = compute_mean(x)
  variance = 0
  for x in x:
    variance = variance + (x - mean)**2
  variance = variance / len(x)
  print("Variance: ", variance)
  return np.sqrt(variance)

x = [171, 176, 155, 167, 169, 182]
print("Standard Deviation: ", np.round(compute_std(x),2))

# use built-in functions in numpy
data = np.array([ 171, 176, 155, 167, 169, 182])

print("Mean: ", np.mean(data))
print("Median: ", np.median(data))
print("Std Deviation: ", np.std(data))
print("Variance: ", np.var(data))

### Question 4

def compute_correlation_cofficient(x, y):
  N = len(x)
  numerator = N * x.dot(y) - np.sum(x)*np.sum(y)
  denominator = np.sqrt(N*np.sum(np.square(x))-np.sum(x)**2) * np.sqrt(N*np.sum(np.square(y))-np.sum(y)**2)

  return np.round(numerator / denominator, 2)

x = np.asarray([-2, -5, -11, 6, 4, 15, 9])
y = np.asarray([4, 25, 121, 36, 16, 225, 81])
print("Correlation: ", compute_correlation_cofficient(x,y))







