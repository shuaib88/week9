import random

def sort(items):
  currentNum = items[0]
  swapCount = 0
  print(items)
  print()

  for i in [0,1,2,3,4,5,6,7,8,9]:
  	currentNum = items[i]
  	if currentNum > items[i+1]:
  		items[i], items[i+1] = items[i+1], items[i]
  		swapCount = swapCount + 1
  	currentNum = items[i+1]
  	print("swap count is", swapCount)
  	print (items)
  	if swapCount != 0:
  		sort(items)

numbers = list(range(10))
random.shuffle(numbers)

assert list(range(10)) == sort(numbers)
print("The list was sorted correctly!")

# 2. Change this print statement to display the complexity category.
#    Refer to the cheat sheet in week9-class for examples.
print("This algorithm is classified as: O(....)")


# another strategy would be do find max and append to new list
