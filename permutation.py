largest_mobile = -1
mobile_index = -1

def sjt(length, graph):
  global largest_mobile, mobile_index
  directions = {i + 1: False for i in range(length)}
  permutation = [i + 1 for i in range(length)]
  hamiltonian_cycles = {} # Where [0] is the permutation and [1] is if it's a Hamiltonian cycle

  while True:
    hamiltonian_cycles[tuple(permutation)] = is_hamiltonian_cycle(permutation, graph)

    largest_mobile = -1
    mobile_index = -1
    findLargestMobileInteger(permutation, directions)

    if largest_mobile == -1:
      break

    # Move the largest mobile element
    if directions[largest_mobile]:  # Moving right
      swap(permutation, permutation.index(largest_mobile), permutation.index(largest_mobile) + 1)
    else:  # Moving left
      swap(permutation, permutation.index(largest_mobile), permutation.index(largest_mobile) - 1)
    
    # Change directions of larger integers
    for i in permutation:
      if i > largest_mobile:
        directions[i] = not directions[i]

  return hamiltonian_cycles

def findLargestMobileInteger(permutation, directions):
  global largest_mobile, mobile_index

  for index in range(0, len(permutation)):
    element = permutation[index]
    
    if directions[element] is False:  # Moving left
      if (index > 0) and (permutation[index] > permutation[index - 1]):
        if permutation[index] > largest_mobile:
          largest_mobile = element
          mobile_index = index
    elif directions[element] is True:  # Moving right
      if (index < len(permutation) - 1) and (permutation[index] > permutation[index + 1]):
        if permutation[index] > largest_mobile:
          largest_mobile = element
          mobile_index = index

def swap(permutation, val1, val2):
  permutation[val1], permutation[val2] = permutation[val2], permutation[val1]

def is_hamiltonian_cycle(permutation, graph):

  # No index can be greater than the length of graph or errors
  for i in range(len(permutation) - 1):
    if permutation[i] >= len(graph):
      return False

  # Check if the cycle visits each vertex exactly once
  if len(permutation) != len(set(permutation)):
    return False
  
  # Check connectivity between consecutive vertices
  for i in range(len(permutation) - 1):
    if not (permutation[i + 1] in graph[permutation[i]][1]):
      return False
          
  # Check that the last vertex connects back to the first vertex
  if not (permutation[0] in graph[permutation[-1]][1]):
    return False
      
  return True

def permutation_start(graph):
  cycles = sjt(len(graph), graph)
  for count, cycle in enumerate(cycles.keys()):
    print(f"Permutation: {count + 1}")
    print(f"\t{cycle}")
    print(f"\tIs Hamiltonian? {cycles[cycle]}")
