import graph_data
import global_game_data
from numpy import random

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

    frontier = [global_game_data.current_player_index]

    visited = set()
    visited.add(global_game_data.current_player_index)

    parents = {}
    parents[global_game_data.current_player_index] = False

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

    while vertex:
        path.insert(0, vertex)
        vertex = parents[vertex]
    
    # Find the exit
    frontier = [target_node_id]
    visited = set()
    visited.add(target_node_id)
    parents = {}
    parents[target_node_id] = False
    while frontier:
        vertex = frontier.pop()

        if vertex == exit_node_id:
            break

        adjacency_list = current_graph[vertex][1]
        for neighbor in adjacency_list:
            if neighbor not in visited:
                visited.add(neighbor)
                parents[neighbor] = vertex
                frontier.append(neighbor)
    
    list_length = len(path)
    while vertex:
        path.insert(list_length, vertex)
        vertex = parents[vertex]

    assert target_node_id in path
    assert exit_node_id in path
    for index in range(len(path) - 1):
        assert path[index+1] in current_graph[index][1]

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

    frontier = [global_game_data.current_player_index]

    visited = set()
    visited.add(global_game_data.current_player_index)

    parents = {}
    parents[global_game_data.current_player_index] = False

    # Find the target
    while frontier:
        vertex = frontier.pop(0)

        if vertex == target_node_id:
            break
        
        adjacency_list = current_graph[vertex][1]
        for neighbor in adjacency_list:
            if neighbor not in visited:
                visited.add(neighbor)
                parents[neighbor] = vertex
                frontier.append(neighbor)

    while vertex:
        path.insert(0, vertex)
        vertex = parents[vertex]
    
    # Find the exit
    frontier = [target_node_id]
    visited = set()
    visited.add(target_node_id)
    parents = {}
    parents[target_node_id] = False
    while frontier:
        vertex = frontier.pop(0)

        if vertex == exit_node_id:
            break

        adjacency_list = current_graph[vertex][1]
        for neighbor in adjacency_list:
            if neighbor not in visited:
                visited.add(neighbor)
                parents[neighbor] = vertex
                frontier.append(neighbor)
    
    list_length = len(path)
    while vertex:
        path.insert(list_length, vertex)
        vertex = parents[vertex]

    assert target_node_id in path
    assert exit_node_id in path
    for index in range(len(path) - 1):
        assert index+1 in current_graph[index][1]

    global_game_data.path_length.append(len(path))
    return path


def get_dijkstra_path():
    return [1,2]
