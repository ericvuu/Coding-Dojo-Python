# 1.
# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

def biggie_size(arr):
    for el in range(len(arr)):
        if arr[el] > 0:
          arr[el] = "big"
    return arr

print(biggie_size([-1, 3, 5, -5]))

# 2.
# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

def count_positives(arr):
      count = 0
      for el in range(len(arr)):
        if arr[el] > 0:
          count += 1

      arr[len(arr) -1] = count
      return arr

print(count_positives([-1,1,1,1]))
print(count_positives([1,6,-4,-2,-7,-2]))

# 3.
# Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

def sum_total(arr):
    total = 0;
    for el in range(len(arr)):
      total += arr[el]
    return total

print(sum_total([1,2,3,4]))
print(sum_total([6,3,-2]))

# 4.
# Average - Create a function that takes a list and returns the average of all the values.x
# Example: average([1,2,3,4]) should return 2.5

def average(arr):
    total = 0
    for el in range(len(arr)):
      total += arr[el]
    return total / len(arr)

print(average([1,2,3,4]))

# 5.
# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0

def length(arr):
    length = 0
    for el in range(len(arr)):
      length += 1
    return length

print(length([37,2,1,-9]))
print(length([]))


# 6.
# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False

def minimum(arr):
    if len(arr) < 1:
      return False
    else:
      min = arr[0]
      for el in range(1,len(arr)):
        if arr[el] < min:
          min = arr[el]
    return min

print(minimum([37,2,1,-9]))
print(minimum([]))

# 7.
# Maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False

def maximum(arr):
    if len(arr) < 1:
      return False
    else:
      max = arr[0]
      for el in range(1,len(arr)):
        if arr[el] > max:
          max = arr[el]
    return max

print(maximum([37,2,1,-9]))
print(maximum([]))

# 8.
# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

def ultimate_analysis(arr):
    sumTotal = arr[0]
    min1 = arr[0]
    max1 = arr[0]
    length = len(arr)


    for el in range(1, len(arr)):
      sumTotal += arr[el]
      # if min is less than current iteration
      if min1 < arr[el]:
        # set max to value in current iteration
        max1 = arr[el]
      else:
        # set the min value to current iteration
        min1 = arr[el]

    average = sumTotal / length

    outputDict = {'sumTotal': sumTotal, 'average': average, 'minimum': min1, 'maximum': max1, 'length': length}
    return outputDict

print(ultimate_analysis([37,2,1,-9]))


# 9.
# Reverse List - Create a function that takes a list and return that list with values reversed.
# Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

import math

def reverse_list(arr):
    # loop through half the array input
    for el in range(0, math.floor(len(arr) / 2)):
      # create a temp variable to store for switching values
      temp = arr[el]
      # reassign current value in iteration to the value in the last position, subtracting one postion each iteration.
      arr[el] = arr[len(arr) - 1 - el]
      # reassign the last position to store the temp variable
      arr[len(arr) - 1 - el] = temp
    return arr

print(reverse_list([37,2,1,-9]))
