import graph_data

def sjt(length):
  global largest_mobile, mobile_index
  permutation = {i + 1: False for i in range(length)}
  hamiltonian_cycles = {} # Where [0] is the permutation and [1] is if it's a Hamiltonian cycle

  while True:
    largest_mobile = -1
    mobile_index = -1 
    findLargestMobileInteger(permutation)

    if largest_mobile == -1:
      break

    # Move the largest mobile element
    if permutation[largest_mobile]:  # Moving right
      swap(permutation, largest_mobile, largest_mobile + 1)
    else:  # Moving left
      swap(permutation, largest_mobile, largest_mobile - 1)
    
    # Change directions of larger integers
    for key in permutation.keys():
      if key > largest_mobile:
        permutation[key] = not permutation[key]
  
    current_perm = tuple(permutation.keys())
    hamiltonian_cycles[current_perm] = is_hamiltonian_cycle(permutation)

  return hamiltonian_cycles

def findLargestMobileInteger(permutation):
  global largest_mobile, mobile_index
  keys = list(permutation.keys())

  for index, element in enumerate(keys):
    if permutation[element] is False:  # Moving left
      if index > 0 and keys[index] > keys[index - 1]:
        if keys[index] > largest_mobile:
          largest_mobile = keys[index]
          mobile_index = index
    elif permutation[element] is True:  # Moving right
      if index < len(keys) - 1 and keys[index] > keys[index + 1]:
        if keys[index] > largest_mobile:
          largest_mobile = keys[index]
          mobile_index = index

def swap(permutation, val1, val2):
  permutation[val1], permutation[val2] = permutation[val2], permutation[val1]

def is_hamiltonian_cycle(permutation):
  n = len(permutation)
  if permutation[1] != 1 or permutation[n] != n:  # Start should be 1 and end should be n
    return False
  for i in range(1, n):
    if permutation[i] + 1 != permutation[i + 1] and permutation[i] - 1 != permutation[i + 1]:
     return False
  return True