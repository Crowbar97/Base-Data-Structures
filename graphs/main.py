from graph import Graph


graph_file_path = 'assets/third.yaml'
g = Graph(graph_file_path)
g.dfs(1)
g.bfs(1)
dists, prevs = g.dij(1)
g.restore_path(prevs, 5)
g.top_sort()