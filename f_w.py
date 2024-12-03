import math

def floyd_warshall_start(current_graph, target_id):
  # Set up the adjacency matrix
  n = len(current_graph)
  adj_matrix = [[math.inf] * n for _ in range(n)]

  for i in range(n):
    adj_matrix[i][i] = 0
    x1, y1 = current_graph[i][0]
    
    for neighbor in current_graph[i][1]:
      x2, y2 = current_graph[neighbor][0]
      distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
      adj_matrix[i][neighbor] = distance
  
  return build_path(floyd_warshall(adj_matrix), 0, target_id, len(current_graph) - 1)

def floyd_warshall(adj_matrix):
  parent_matrix = [[None for i in range(len(adj_matrix))] for j in range(len(adj_matrix))]

  for k in range(len(adj_matrix)):
    for i in range(len(adj_matrix)):
      for j in range(len(adj_matrix)):
          if adj_matrix[i][k] + adj_matrix[k][j] < adj_matrix[i][j]:
            adj_matrix[i][j] = adj_matrix[i][k] + adj_matrix[k][j]
            parent_matrix[i][j] = k

  return parent_matrix

def build_path(parent_matrix, start, target, end):
  def build_subpath(parent_matrix, start, end):
    path = []
    current = parent_matrix[start][end]
    while current is not None:
      path.insert(0, current)
      current = parent_matrix[start][current]
    path.insert(0, start)
    path.append(end)
    return path

  path_to_target = build_subpath(parent_matrix, start, target)
  path_to_exit = build_subpath(parent_matrix, target, end)
  full_path = path_to_target + path_to_exit[1:]

  return full_path
