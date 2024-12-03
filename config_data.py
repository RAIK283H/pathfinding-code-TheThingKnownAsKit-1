import colors
window_width = 1400
window_height = 900
starting_player_index = 0
starting_graph_index = 0

player_data = [
    ["Test", "1.png", colors.YELLOW],
    ["Floyd-Warshall", "5.png", colors.GREEN]
]

# These are still loaded as part of player_data length so it
# produces an error in graph.py when trying to display players
# copied original player_data down here so I could delete it above
# player_data = [
#     ["Test", "1.png", colors.YELLOW],
#     # ["Random", "2.png", colors.ORANGE],
#     # ["DFS", "3.png", colors.PURPLE],
#     # ["BFS", "4.png", colors.BLUE],
#     ["Floyd-Warshall", "5.png", colors.GREEN]
# ]

display_size_right = 400
display_size_bottom = 100
display_size_top = 0
display_size_left = 0
graph_padding = 60
player_speed = 7