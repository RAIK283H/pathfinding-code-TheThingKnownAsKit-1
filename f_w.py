import math

def floyd_warshall_start(current_graph, target_id):
  # Set up the adjacency matrix
  n = len(current_graph)
  adj_matrix = [[None] * n for _ in range(n)]

  for i in range(n):
    adj_matrix[i][i] = 0
    x1, y1 = current_graph[i][0]
    
    for neighbor in current_graph[i][1]:
      x2, y2 = current_graph[neighbor][0]
      distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
      adj_matrix[i][neighbor] = distance
  
  return build_path(floyd_warshall(adj_matrix), current_graph[0], target_id, current_graph[len(current_graph) - 1])

def floyd_warshall(adj_matrix):
  parent_matrix = [[None if i == j or adj_matrix[i][j] is None else i for j in range(len(adj_matrix))] for i in range(len(adj_matrix))]

  for k in range(len(adj_matrix) - 1):
    for i in range(len(adj_matrix) - 1):
      for j in range(len(adj_matrix) - 1):
        if adj_matrix[i][k] is not None and adj_matrix[k][j] is not None:
          new_distance = adj_matrix[i][k] + adj_matrix[k][j]
          if adj_matrix[i][j] is None or new_distance < adj_matrix[i][j]:
            adj_matrix[i][j] = new_distance
            parent_matrix[i][j] = parent_matrix[k][j]

  return parent_matrix

def build_path(parent_matrix, start, target, end):
  def build_subpath(parent_matrix, start, end):
    path = []
    while end is not None:
      path.insert(0, end)
      end = parent_matrix[start][end]
    return path

  path_to_target = build_subpath(parent_matrix, start, target)
  path_to_exit = build_subpath(parent_matrix, target, end)
  full_path = path_to_target + path_to_exit[1:]

  return full_path
