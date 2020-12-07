prices_fare = [
  49.5, 57.0, 16.7, 134.5, 52.0, 
  26.55, 151.55, 78.85, 52.55, 12.47, 
  153.46, 227.53, 113.28, 30.0, 53.1, 
  26.55, 50.5, 8.05, 25.93, 83.16, 
  86.5, 110.88, 53.1, 247.52, 13.0, 
  52.0, 110.88, 40.12, 53.1, 75.25, 
  25.93, 10.5, 76.73, 39.6, 120.0, 
  52.0, 12.47, 93.5, 52.55, 39.4, 
  135.63, 77.29, 71.0, 76.73, 120.0, 
  151.55, 153.46, 90.0, 90.0, 77.96
  ]
passengers_age = [
  22.0, 17.0, 24.0, 40.0, 48.0, 
  45.0, 25.0, 36.0, 47.0, 6.0, 
  40.0, 18.0, 23.0, 19.0, 19.0, 
  28.0, 31.0, 32.0, 48.0, 56.0, 
  33.0, 49.0, 35.0, 50.0, 32.5, 
  47.0, 17.0, 36.0, 37.0, 60.0, 
  49.0, 57.0, 49.0, 48.0, 11.0, 
  31.0, 27.0, 30.0, 37.0, 16.0, 
  36.0, 21.0, 70.0, 27.0, 36.0, 
  2.0, 38.0, 38.0, 44.0, 63.0
  ]
standard_deviation_fare = 53.05
standard_deviation_age = 14.80

def de_mean(x):
    # x_bar is the mean of x
    x_bar = sum(x) / len(x)
    return [x_i - x_bar for x_i in x]

def dot(x,y):
    return sum(x_i * y_i for x_i, y_i in zip(x, y))

def covariance(x, y):
    n = len(x)
    # return the covariance of x and y
    return dot(de_mean(x), de_mean(y)) / (n - 1)

def correlation(x, y):
    # return the correlation
    return covariance(x,y) / stdev_fare / stdev_age

print("In the two lists")
print("The correlation of prices and age is ：")
print(correlation(prices_fare, passengers_age)) 
