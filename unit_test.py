import math
import unittest
import global_game_data
import graph_data
import pathing


class TestPathFinding(unittest.TestCase):
    def setUp(self):
        # Set the current graph index for testing
        self.graphs = graph_data.graph_data
        global_game_data.current_graph_index = 0  # Start with the first graph
        global_game_data.target_node = [2]  # Example target node (can be changed for other tests)
        global_game_data.current_player_index = 0  # Starting at node 0
        global_game_data.graph_paths = []
        global_game_data.path_length = []

    def test_upper(self):
        self.assertEqual('test'.upper(), 'TEST')

    def test_isupper(self):
        self.assertTrue('TEST'.isupper())
        self.assertFalse('Test'.isupper())

    def test_floating_point_estimation(self):
        first_value = 0
        for x in range(1000):
            first_value += 1/100
        second_value = 10
        almost_pi = 3.1
        pi = math.pi
        self.assertNotEqual(first_value,second_value)
        self.assertAlmostEqual(first=first_value,second=second_value,delta=1e-9)
        self.assertNotEqual(almost_pi, pi)
        self.assertAlmostEqual(first=almost_pi, second=pi, delta=1e-1)
    
    def test_dfs_path(self):
        pathing.set_current_graph_paths()  # Populate graph paths
        path = pathing.get_dfs_path()
        
        # Validate the path for DFS
        expected_dfs_path = [1, 2, 2]  # Adjust based on your DFS logic
        self.assertEqual(path, expected_dfs_path)
    
    def test_bfs_path(self):
        pathing.set_current_graph_paths()  # Populate graph paths
        path = pathing.get_bfs_path()
        
        # Validate the path for BFS
        expected_bfs_path = [1, 2, 2]  # Adjust based on your BFS logic
        self.assertEqual(path, expected_bfs_path)

if __name__ == '__main__':
    unittest.main()
