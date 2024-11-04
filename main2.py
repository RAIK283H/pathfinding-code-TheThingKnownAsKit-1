import graph_data
import global_game_data
from permutation import permutation_start

def main():
  current_graph = graph_data.graph_data[global_game_data.current_graph_index]
  permutation_start(current_graph)

if __name__ == '__main__':
  main()