tickets_price = [
  56.5, 7.75, 133.65, 8.85, 7.9, 
  15.5, 10.5, 7.9, 7.75, 27.75, 
  7.9, 30.5, 8.65, 13.0, 27.72, 
  18.0, 15.74, 23.0, 30.5, 9.59, 
  7.05, 7.72, 120.0, 10.5, 7.75, 
  151.55, 7.9, 7.9, 89.1, 34.38, 
  8.03, 73.5, 7.8, 7.78, 7.22, 
  52.0, 24.15, 8.05, 7.9, 39.0, 
  9.5, 7.75, 15.85, 17.8, 21.68, 
  7.75, 7.55, 7.75, 10.5, 7.05
  ]
# tease out the set of prices and try to delete those abnormal ones
# the function that finds out the n percentile numbers
def find_nperc(numbers,n):
  
    # sort the list
    sorted_numbers = sorted(numbers)
    
    # find the index of the n percentile
    n_index = int(n/100 * len(sorted_numbers))
    
    return sorted_numbers[n_index]

# assume the 25 percentile value as quarter1_price
quarter1_price = find_nperc(tickets_price,25)

# assume the 75 percentile value as quarter3_price
quarter3_price = find_nperc(td_price,75)

# assume difference as the range between quarter1_price and quarter3_price
difference = quarter3_price - quarter1_price

for price in tickets_price:
    if price > quarter3_price + 1.5 * difference or price < quarter1_price - 1.5 * difference:
        tickets_price.remove(price)
        print("delete abnormal value {}".format(price))

# compute the average price of the corrected list
average_price = round(sum(tickets_price) / len(tickets_price),2)
print("The average price(pounds) of tickets is {}".format(average_price))

# compute the face value of the mean price, time it by 100
current_value_of_one_ticket = average_price * 100
print("The face value(pounds) of one ticket is {}".format(current_value_of_one_ticket))
