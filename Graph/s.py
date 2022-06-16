UNEXPLORED, VISITED = 'unxp', 'vstd'  # for vertex
DISCOVERY, BACK = 'dscv', 'back'  # for edge

# Initialize Vertex and Edge Labels
N = 3
V_label = [UNEXPLORED for _ in range(N)]
E_label = [[UNEXPLORED for _ in range(N)] for _ in range(N)]

# Vertex Visiting Order during DFS
print(V_label)
print(E_label)
