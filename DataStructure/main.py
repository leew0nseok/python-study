class Graph:
	def __init__(self, N=1000):
		self.N = N
		# Create 2D list M: M[i][j] = 1, if edge (i,j) exists
		self.M = [[0 for _ in range(N)] for _ in range(N)]
	
	def insert_edge(self, v1, v2):
		# this is an undirected graph
		#therefore, mark both (v1, v2) and (v2, v1)
		self.M[v1][v2] = 1
		self.M[v2][v1] = 1
		pass
	
	def adjacent_vertices(self, v):	
		vs = []
		for j in range(self.N): # return the adjacent (or linked) vertices to v
			if self.M[v][j] == 1: # [j][v]해도 가능할거로 생각함.
				vs.append(j)
		return vs
	

class DFS:
	def __init__(self, G):
		# Graph Info
		self.G = G
		self.N = G.N
		
		# Vertex and Edge Labels
		# FOR LABELING, use EXACTLY these labels
		self.UNEXPLORED, self.VISITED = 'unxp', 'vstd' #for vertex
		self.DISCOVERY, self.BACK = 'dscv', 'back' #for edge
		
		# Initialize Vertex and Edge Labels 
		self.V_label = [self.UNEXPLORED for _ in range(N)]
		self.E_label = [[self.UNEXPLORED for _ in range(N)] for _ in range(N)]
		
		# Vertex Visiting Order during DFS
		self.visit_order = []
		
		# Run DFS
		for v in range(self.N):
			if self.V_label[v] == self.UNEXPLORED:
				self.dfs(v)
		
	def dfs(self, v):
		self.V_label[v] = self.VISITED
		self.visit_order.append(v)
		
		v_adj = self.G.adjacent_vertices(v)
		for w in v_adj:
			if self.E_label[v][w] == self.UNEXPLORED and self.E_label[w][v] == self.UNEXPLORED:
				if self.V_label[w] == self.UNEXPLORED:
					self.E_label[v][w] = self.DISCOVERY
					self.dfs(w)
				else:
					self.E_label[v][w] = self.BACK
