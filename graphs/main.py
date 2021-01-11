from graph import Graph


graph_file_path = 'assets/third.yaml'
g = Graph(graph_file_path)
# g.dfs(1)
# g.bfs(1)
# g.dij(1)
g.top_sort()