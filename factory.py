class SolverFactory:
	def __init__(self):
		self.Default = "breadthfirst";
		self.Choices = ["breadthfirst","depthfirst","dijkstra", "astar","leftturn"];

	def createsolver(self, type):
		if type == "leftturn":
			import leftturn;
			return ["Left Turn Only", leftturn.solve];
		elif type == "depthfirst":
			import depthfirst;
			return ["Depthfirst Search", depthfirst.solve];
		elif type == "dijkstra":
			import dijkstra;
			return ["Dijkstra's Algorithm", dijkstra.solve];
		elif type == "astar":
			import astar;
			return ["A-Star Search", astar.solve];
		else:
			import breadthfirst;
			return ["Breadthfirst Search", breadthfirst.solve];