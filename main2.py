import graph_data
import global_game_data
import permutation

def main():
  cycles = permutation.sjt(3, graph_data.graph_data[global_game_data.current_graph_index])
  print(cycles)

if __name__ == '__main__':
  main()