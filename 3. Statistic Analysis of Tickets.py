# list fare_survivors stores the prices of some survivors' tickets, while list fare_victims stores the prices of some victims' tickets

fare_survivors = [
  39.6, 79.65, 26.0, 49.5, 108.9, 
  211.34, 30.5, 63.36, 53.1, 16.7, 
  135.63, 49.5, 75.25, 83.16, 35.5, 
  53.1, 39.0, 57.98, 93.5, 26.39, 
  26.55, 39.4, 134.5, 90.0, 56.93, 
  83.16, 26.55, 77.96, 8.05, 120.0, 
  57.0, 12.47, 135.63, 55.0, 153.46, 
  512.33, 30.0, 55.44, 512.33, 262.38, 
  25.93, 78.27, 26.28, 83.47, 89.1, 
  26.55, 26.55, 247.52, 262.38, 13.0, 
  30.0, 86.5, 55.9, 51.48, 26.0, 
  263.0, 25.93, 91.08, 10.5, 146.52, 
  69.3, 10.5, 227.53, 77.96, 151.55
  ]


fare_victims = [
  151.55, 110.88, 61.98, 263.0, 52.0, 
  38.5, 77.29, 247.52, 32.32, 26.55, 
  26.55, 79.65, 34.65, 66.6, 33.5, 
  106.42, 25.59, 26.55, 7.65, 0.0, 
  10.46, 27.75, 30.7, 113.28, 108.9, 
  77.29, 29.7, 35.5, 10.5, 30.0, 
  79.2, 211.5, 30.5, 40.12, 5.0
  ]
  
# compute the range of list fare_survivors
range_survival_fare = max(fare_survivors) - min(fare_survivors)

# compute the range of list fare_victims
range_victim_fare = max(fare_victims) - min(fare_victims)

# compute the average ticket price of list fare_survivors
mean_survival_fare = sum(fare_survivors) / len(fare_survivors)

# compute the average ticket price of list fare_victims
mean_victims_fare = sum(fare_victims) / len(fare_victims)

# compute the variance and standard deviation of list fare_survivors, and put them into variables "variance_survival_fare" and "standard_deviation_fare_survival"
sum_variance_survival_fare = 0
for fare in fare_survivors:
    sum_variance_survival_fare += (fare - mean_survival_fare) ** 2
variance_survival_fare = sum_variance_survival_fare / (len(fare_survivors) - 1)
standard_deviation_fare_survival = variance_survival_fare ** 0.5

# compute the variance and standard deviation of list fare_victims, and put them into variables "variance_victim_fare" and "standard_deviation_fare_victim"
sum_variance_victim_fare = 0
for fare in fare_victims:
  sum_variance_victim_fare += (fare - mean_victims_fare) **2
variance_victim_fare = sum_variance_victim_fare / (len(fare_victims)-1)
standard_deviation_fare_victim = variance_victim_fare **0.5

print("Statistics of a set of tickets of survivors in Titanic disaster：")
print("the mean is：{}".format(round(mean_survival_fare,2)))
print("the range is：{}".format(round(range_survival_fare,2)))
print("the variance is：{}".format(round(variance_survival_fare,2)))
print("the standard deviation is：{}".format(round(standard_deviation_fare_survival,2)))

print("Statistics of a set of tickets of victims in Titanic disaster：")
print("the mean is：{}".format(round(mean_victims_fare,2)))
print("the range is：{}".format(round(range_victim_fare,2)))
print("the variance is：{}".format(round(variance_victim_fare,2)))
print("the standard deviation is：{}".format(round(standard_deviation_fare_victim,2)))
