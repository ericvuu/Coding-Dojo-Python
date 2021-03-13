
arr = [6,5,3,1,8,7,2,4]

# start at index 1 of array
for i in range(1,len(arr)):

  compVal = arr[i]

  # check if previous positions are larger than the current position
  # set starting loop value to index before position of i
  j = i - 1
  while j >= 0 and arr[j] > compVal:
    # if the previous position is larger, move the previous value to next position ahead
    # reassign forward index to value of previous value
    arr[j + 1] = arr[j]
    # continue the comparisons until base case of current iteration is reached by decrementing j
    j -= 1
  # reassign previous index to value of comparison value set by outer loop
  arr[j + 1] = compVal

print(arr)
