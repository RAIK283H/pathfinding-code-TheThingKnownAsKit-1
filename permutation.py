permutation = {} # False is left, True is right
largest_mobile = -1
mobile_index = -1

def sjt(length):
  permutation = {i + 1: False for i in range(length)}

  while largest_mobile is not -1:
    largest_mobile = -1
    mobile_index = -1 
    findLargestMobileInteger()

    # Move the largest mobile
    if permutation[largest_mobile] is True: # Moving right
      permutation[mobile_index], permutation[mobile_index + 1] = permutation[mobile_index + 1], permutation[mobile_index]
      mobile_index += 1
    else: # Moving left
      permutation[mobile_index + 1], permutation[mobile_index] = permutation[mobile_index], permutation[mobile_index + 1]
      mobile_index -= 1
    
    # Swap directions of larger integers
    for element in enumerate(permutation):
      if element > largest_mobile:
        permutation[element] = not permutation[element]

def findLargestMobileInteger():
  keys = permutation.keys()

  for index, element in enumerate(permutation.keys()):
    if permutation[element] is False:
      if (index > 0) and (keys[index] > keys[index + 1]) and (keys[index] > largest_mobile):
        largest_mobile = element
        mobile_index = index
    elif permutation[element] is True:
      if (index < len(permutation) - 1) and (keys[index] > keys[index + 1]) and (keys[index] > largest_mobile):
        largest_mobile = element
        mobile_index = index