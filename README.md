# Pathfinding Starter Code
The random path algorithm works by first searching the graph for the target node, and
then searching the graph for the exit node. If the target or exit node is within the
current node's adjacency list, go to it, otherwise pick randomly from the adjacency list.
There is frequent backtracking and looping with this implementation, which is allowed.

The new statistic is the length (in steps/nodes visited) of the path a player takes.

Extra credit for HW 7. Implemented Floyd-Warshall in place of the Dijkstra player