import math
import unittest
import global_game_data
import graph_data
import pathing
import permutation

class TestPathFinding(unittest.TestCase):
    def setUp(self):
        # Sample graphs for testing
        self.graph_1 = [
            [(0, 0), [1, 2]],
            [(100, 100), [0, 2]],
            [(200, 100), [0, 1]],
        ]

        self.graph_2 = [
            [(0, 0), [1, 3]],
            [(100, 100), [0, 2]],
            [(100, 200), [1, 3]],
            [(200, 200), [0, 2]]
        ]

        self.graph_3 = [
            [(0, 0), [1]],
            [(100, 100), [0, 2, 3]],
            [(200, 100), [1, 3]],
            [(300, 0), [1, 2, 4]],
            [(300, 100), [3]]
        ]

        global_game_data.current_graph_index = 0
        global_game_data.target_node = [1]
        global_game_data.current_player_index = 0 
        global_game_data.graph_data = [self.graph_1, self.graph_2, self.graph_3]

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
        expected_dfs_path = [1, 2]
        dfs_path = pathing.get_dfs_path()
        
        self.assertEqual(dfs_path, expected_dfs_path)
    
    def test_bfs_path(self):
        expected_bfs_path = [1, 2]
        bfs_path = pathing.get_bfs_path()
        
        self.assertEqual(bfs_path, expected_bfs_path)
    
    def test_dijkstra_path(self):
        expected_dijkstra_path = [0, 1, 2]
        dijkstra_path = pathing.get_dijkstra_path()

        self.assertEqual(dijkstra_path, expected_dijkstra_path)

    def test_hamiltonian_cycle(self):
        cycle_1_correct = [0, 1]
        cycle_1_incorrect = [1, 0, 2, 1]
        cycle_2_correct = [0, 1, 2, 3]
        cycle_2_incorrect = [0, 1, 3, 2, 3]

        self.assertTrue(permutation.is_hamiltonian_cycle(cycle_1_correct, self.graph_1))
        self.assertFalse(permutation.is_hamiltonian_cycle(cycle_1_incorrect, self.graph_1))
        self.assertTrue(permutation.is_hamiltonian_cycle(cycle_2_correct, self.graph_2))
        self.assertFalse(permutation.is_hamiltonian_cycle(cycle_2_incorrect, self.graph_2))
    
    def test_permutations(self):
        permutations = permutation.sjt(len(self.graph_1), self.graph_1)
        permutations = list(permutations.keys())
        expected = [
            [1, 2, 3],
            [1, 3, 2],
            [3, 1, 2],
            [3, 2, 1],
            [2, 3, 1],
            [2, 1, 3]
        ]

        self.assertEqual(len(permutations), len(expected))
        for perm in range(len(permutations)):
            for i in range(len(permutations[perm])):
                self.assertEqual(permutations[perm][i], expected[perm][i])

if __name__ == '__main__':
    unittest.main()
