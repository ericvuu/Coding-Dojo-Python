arr = [8,5,2,6,9,3,1,4,7]

print(arr)

# iterate through the unsorted array
for i in range(len(arr)):

  # iterate through the array and find the first index will a smaller value
  for j in range(i+1, len(arr)):

    # if i larger than current j value
    if arr[i] > arr[j]:
      # set temp variable to i
      temp = arr[i]
      # set i to j
      arr[i] = arr[j]
      # set j to temp
      arr[j] = temp

print(arr)
