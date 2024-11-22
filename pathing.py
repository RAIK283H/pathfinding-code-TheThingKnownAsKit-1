import graph_data
import global_game_data
from numpy import random
import heapq as heap
import math

def set_current_graph_paths():
    global_game_data.graph_paths.clear()
    global_game_data.graph_paths.append(get_test_path())
    global_game_data.graph_paths.append(get_random_path())
    global_game_data.graph_paths.append(get_dfs_path())
    global_game_data.graph_paths.append(get_bfs_path())
    global_game_data.graph_paths.append(get_dijkstra_path())


def get_test_path():
    path = graph_data.test_path[global_game_data.current_graph_index]
    global_game_data.path_length.append(len(path))
    return path


def get_random_path():
    assert global_game_data is not None
    assert graph_data is not None

    current_graph_index = global_game_data.current_graph_index
    current_graph = graph_data.graph_data[current_graph_index]
    target_node_id = global_game_data.target_node[current_graph_index]
    exit_node_id = len(current_graph) - 1
    
    current_node_id = 0
    path = [current_node_id]

    found_target = False
    while (not found_target):
        adjacency_list = current_graph[current_node_id][1]

        if (target_node_id in adjacency_list):
            path.append(target_node_id)
            found_target = True
        else:
            next = random.choice(adjacency_list)
            path.append(next)
            current_node_id = next
    
    found_exit = False
    while (not found_exit):
        adjacency_list = current_graph[current_node_id][1]

        if (exit_node_id in adjacency_list):
            path.append(exit_node_id)
            found_exit = True
        else:
            next = random.choice(adjacency_list)
            path.append(next)
            current_node_id = next

    assert path is not None
    assert 0 in path
    assert target_node_id in path
    assert exit_node_id in path

    global_game_data.path_length.append(len(path))
    return path


def get_dfs_path():
    assert global_game_data is not None
    assert graph_data is not None

    current_graph_index = global_game_data.current_graph_index
    current_graph = graph_data.graph_data[current_graph_index]
    target_node_id = global_game_data.target_node[current_graph_index]
    exit_node_id = len(current_graph) - 1
    path = []

    frontier = []
    frontier.insert(0, 0)

    visited = set()
    visited.add(0)

    parents = {}
    parents[0] = False

    # Find the target
    while frontier:
        vertex = frontier.pop()

        if vertex == target_node_id:
            break
        
        adjacency_list = current_graph[vertex][1]
        for neighbor in adjacency_list:
            if neighbor not in visited:
                visited.add(neighbor)
                parents[neighbor] = vertex
                frontier.append(neighbor)

    vertex = target_node_id
    while vertex:
        path.insert(0, vertex)
        vertex = parents[vertex]
    
    # Find the exit
    parents = {}
    parents[target_node_id] = vertex
    frontier = []
    frontier.insert(0, target_node_id)
    visited = set()
    visited.add(target_node_id)
    while frontier:
        vertex = frontier.pop()

        if vertex == exit_node_id:
            break

        adjacency_list = current_graph[vertex][1]
        for neighbor in adjacency_list:
            if neighbor not in visited:
                visited.add(neighbor)
                parents[neighbor] = vertex
                frontier.insert(0, neighbor)
    
    vertex = exit_node_id
    while vertex:
        path.insert(0, vertex)
        vertex = parents[vertex]

    assert target_node_id in path
    assert exit_node_id in path
    assert is_all_connected(path, current_graph)

    global_game_data.path_length.append(len(path))
    return path


def get_bfs_path():
    assert global_game_data is not None
    assert graph_data is not None

    current_graph_index = global_game_data.current_graph_index
    current_graph = graph_data.graph_data[current_graph_index]
    target_node_id = global_game_data.target_node[current_graph_index]
    exit_node_id = len(current_graph) - 1
    path = []

    frontier = []
    frontier.insert(0, 0)

    visited = set()
    visited.add(0)

    parents = {}
    parents[0] = False

    # Find the target
    while frontier:
        vertex = frontier.pop()

        if vertex == target_node_id:
            break
        
        adjacency_list = current_graph[vertex][1]
        for neighbor in adjacency_list:
            if neighbor not in visited:
                visited.add(neighbor)
                parents[neighbor] = vertex
                frontier.insert(0, neighbor)

    vertex = target_node_id
    while vertex:
        path.insert(0, vertex)
        vertex = parents[vertex]
    
    # Find the exit
    parents = {}
    parents[target_node_id] = vertex
    frontier = []
    frontier.insert(0, target_node_id)
    visited = set()
    visited.add(target_node_id)
    while frontier:
        vertex = frontier.pop()

        if vertex == exit_node_id:
            break

        adjacency_list = current_graph[vertex][1]
        for neighbor in adjacency_list:
            if neighbor not in visited:
                visited.add(neighbor)
                parents[neighbor] = vertex
                frontier.insert(0, neighbor)
    
    vertex = exit_node_id
    while vertex:
        path.insert(0, vertex)
        vertex = parents[vertex]

    assert target_node_id in path
    assert exit_node_id in path
    assert is_all_connected(path, current_graph)

    global_game_data.path_length.append(len(path))
    return path

def get_dijkstra_path():
    assert global_game_data is not None
    assert graph_data is not None

    current_graph_index = global_game_data.current_graph_index
    current_graph = graph_data.graph_data[current_graph_index]
    target_node_id = global_game_data.target_node[current_graph_index]
    exit_node_id = len(current_graph) - 1
    path = []

    frontier = []
    heap.heapify(frontier)
    heap.heappush(frontier, (0, 0, 0))
    visited = set()
    parents = {0: False}
    distances = {0: 0}

    while frontier:
        current_cost, vertex, tie_breaker = heap.heappop(frontier)
        if vertex in visited:
            continue
        visited.add(vertex)

        if vertex == target_node_id:
            break
    
        adjacency_list = current_graph[vertex][1]
        for neighbor in adjacency_list:
            if neighbor in visited:
                continue

            vertex_coords = current_graph[vertex][0]
            neighbor_coords = current_graph[neighbor][0]
            target_coords = current_graph[target_node_id][0]
            distance = math.sqrt((neighbor_coords[0] - vertex_coords[0])**2 + (neighbor_coords[1] - vertex_coords[1])**2)
            new_cost = current_cost + distance

            tie_distance = math.sqrt((target_coords[0] - neighbor_coords[0])**2 + (target_coords[1] - neighbor_coords[1])**2)

            if neighbor not in distances or new_cost < distances[neighbor]:
                distances[neighbor] = new_cost
                parents[neighbor] = vertex
                heap.heappush(frontier, (new_cost, neighbor, tie_distance))
            elif new_cost == distances[neighbor] and tie_distance < distances[neighbor]:
                # Tie-breaking logic
                distances[neighbor] = new_cost
                parents[neighbor] = vertex
                heap.heappush(frontier, (new_cost, neighbor, tie_distance))

    vertex = target_node_id
    while vertex:
        path.insert(0, vertex)
        vertex = parents[vertex]
    
    # Find the exit
    frontier = []
    heap.heapify(frontier)
    heap.heappush(frontier, (0, target_node_id, 0))
    visited = set()
    parents = {}
    parents[target_node_id] = False
    distances = {target_node_id: 0}
    while frontier:
        current_cost, vertex, tie_breaker = heap.heappop(frontier)
        if vertex in visited:
            continue
        visited.add(vertex)

        if vertex == exit_node_id:
            break
    
        adjacency_list = current_graph[vertex][1]
        for neighbor in adjacency_list:
            if neighbor in visited:
                continue

            vertex_coords = current_graph[vertex][0]
            neighbor_coords = current_graph[neighbor][0]
            exit_coords = current_graph[exit_node_id][0]
            distance = math.sqrt((neighbor_coords[0] - vertex_coords[0])**2 + (neighbor_coords[1] - vertex_coords[1])**2)
            new_cost = current_cost + distance

            tie_distance = math.sqrt((exit_coords[0] - neighbor_coords[0])**2 + (exit_coords[1] - neighbor_coords[1])**2)

            if neighbor not in distances or new_cost < distances[neighbor]:
                distances[neighbor] = new_cost
                parents[neighbor] = vertex
                heap.heappush(frontier, (new_cost, neighbor, tie_distance))
            elif new_cost == distances[neighbor] and tie_distance < distances[neighbor]:
                # Tie-breaking logic
                distances[neighbor] = new_cost
                parents[neighbor] = vertex
                heap.heappush(frontier, (new_cost, neighbor, tie_distance))
    
    vertex = exit_node_id
    length = len(path) - 1
    while vertex:
        path.insert(length, vertex)
        vertex = parents[vertex]

    assert target_node_id in path
    assert exit_node_id in path
    assert is_all_connected(path, current_graph)

    path.pop()
    global_game_data.path_length.append(len(path))
    return path

def is_all_connected(path, graph):
    for i in range(len(path) - 2):
        if not (path[i] in graph[path[i + 1]][1]):
            return False
    return True