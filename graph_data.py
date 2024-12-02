'''
graph_data[a] = gives you graph at index a
graph_data[a][0] = start node of graph a
graph_data[a][length-1] = exit node of graph a
graph_data[a][b][0] = x-y coordinates as tuple of point b in graph a
graph_data[a][b][1] = adjacency list of point b in graph a

Only the start and exit nodes are dead ends (all other nodes have degree >= 2)
'''


graph_data = [
    [
        [(0, 0), [1]],
        [(200, -200), [0, 2]],
        [(200, -400), [1]]
    ],
    [
        [(0, 0), [1]],
        [(50, -200), [0, 2]],
        [(50, -300), [1, 3]],
        [(200, -500), [2]]
    ],
    [
        [(900, 45), [17, 21, 22]],
        [(70, 350), [2, 7, 19, 20]],
        [(140, 420), [1, 5, 9, 10, 20]],
        [(210, 70), [6, 8, 11, 22]],
        [(210, 210), [6, 7, 11, 12, 20]],
        [(210, 490), [2, 10, 21]],
        [(280, 140), [3, 4, 11, 20]],
        [(280, 280), [1, 4, 9, 12, 20]],
        [(350, 70), [3, 11]],
        [(350, 350), [2, 7, 10, 12, 13, 15]],
        [(350, 490), [2, 5, 9, 13, 14, 15]],
        [(420, 140), [3, 4, 6, 8, 12, 16, 17]],
        [(420, 280), [4, 7, 9, 11, 15, 17]],
        [(420, 420), [9, 10, 15]],
        [(490, 490), [10, 18, 15]],
        [(560, 420), [9, 10, 12, 13, 14, 17, 18]],
        [(630, 70), [11, 17]],
        [(630, 210), [11, 12, 15, 16, 18, 0]],
        [(700, 420), [14, 15, 17, 23]],
        [(70, 500), [1, 21]],
        [(70, 210), [1, 2, 4, 6, 7, 22]],
        [(450, 700), [5, 19, 0, 23]],
        [(45, 45), [0, 3, 20]],
        [(1225, 700), [18, 21]]
    ],
    [
        [(0, 0), [1, 4]],
        [(0, 100), [0, 2, 5]],
        [(0, 200), [1, 3, 6]],
        [(0, 300), [2, 7]],
        [(100, 0), [5, 0, 8]],
        [(100, 100), [4, 6, 1, 9]],
        [(100, 200), [5, 7, 2, 10]],
        [(100, 300), [6, 3, 11]],
        [(200, 0), [9, 4, 12]],
        [(200, 100), [8, 10, 5, 13]],
        [(200, 200), [9, 11, 6, 14]],
        [(200, 300), [10, 7, 15]],
        [(300, 0), [13, 8]],
        [(300, 100), [12, 14, 9]],
        [(300, 200), [13, 15, 10]],
        [(300, 300), [14,11]],
    ],
    [
        [(45, 45), [1]],
        [(100, 245), [0, 2, 4]],
        [(200, 245), [1, 3, 5]],
        [(300, 145), [2, 6]],
        [(100, 345), [1, 5, 7]],
        [(200, 345), [2, 4, 6, 8]],
        [(300, 345), [3, 9]],
        [(100, 545), [4, 8]],
        [(200, 445), [5, 7, 9]],
        [(300, 445), [6, 8, 10]],
        [(1200, 700), [9]]
    ],
    [
        [(45, 45), [1]],
        [(100, 245), [14, 0, 2]],
        [(200, 245), [1, 5, 3]],
        [(300, 245), [2, 6, 10, 11, 12]],
        [(500, 345), [13, 6, 9]],
        [(200, 345), [14, 2, 6, 8]],
        [(300, 345), [9, 5, 4, 3]],
        [(100, 545), [8, 14]],
        [(200, 445), [5, 7, 9]],
        [(300, 445), [4, 6, 8, 15]],
        [(200, 145), [3, 11]],
        [(300, 145), [3, 10, 12]],
        [(400, 145), [3, 11, 13]],
        [(500, 145), [4, 12]],
        [(100, 345), [1, 7, 5]],
        [(1200, 700), [9]],
    ],
    [
        [(0, 0), [1]],
        [(100, 100), [0, 2, 4]],
        [(200, 0), [1, 3]],
        [(300, 100), [2, 5]],
        [(100, 200), [1, 6]],
        [(200, 200), [3, 7, 8]],
        [(100, 300), [4, 9]],
        [(300, 200), [5]],
        [(200, 300), [5]],
        [(0, 400), [6]]
    ],
    [
        [(50, 50), [1]],
        [(50, 150), [0, 2, 3]],
        [(150, 150), [1, 4]],
        [(50, 250), [1, 5]],
        [(150, 250), [2, 6]],
        [(250, 150), [3, 7]],
        [(250, 250), [4, 8]],
        [(300, 200), [5, 9]],
        [(300, 300), [6]],
        [(400, 200), [7]]
    ],
    [
        [(0, 0), [1, 5]],
        [(100, 0), [0, 2]],
        [(100, 100), [1, 3]],
        [(100, 200), [2, 4]],
        [(200, 200), [3, 5]],
        [(200, 0), [0, 4, 6]],
        [(300, 0), [5, 7]],
        [(300, 100), [6, 8]],
        [(300, 200), [7, 9]],
        [(400, 200), [8, 10]],
        [(400, 100), [9, 11]],
        [(400, 0), [10, 12]],
        [(500, 0), [11, 13]],
        [(500, 100), [12, 14]],
        [(500, 200), [13, 15]],
        [(600, 200), [14, 16]],
        [(600, 100), [15, 17]],
        [(600, 0), [16, 18]],
        [(700, 0), [17, 19]],
        [(700, 100), [18, 20]],
        [(700, 200), [19, 21]],
        [(800, 200), [20, 22]],
        [(800, 100), [21, 23]],
        [(800, 0), [22, 24]],
        [(900, 0), [23]]
    ]
]

test_path = [
    [1, 2],
    [1, 2, 3],
    [22, 3, 11, 17, 18, 23],
    [1, 5, 6, 10, 11, 15],
    [1, 2, 5, 8, 9, 10],
    [1, 14, 5, 6, 9, 15],
    [1, 4, 6, 9],
    [1, 3, 5, 7, 9],
    [1, 6, 8, 9, 11, 12, 14, 15, 17, 18, 20, 21, 23, 24]
]
