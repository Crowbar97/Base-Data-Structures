import json


class Graph:
    def __init__(self, graph_file_path):
        with open(graph_file_path) as graph_file:
            self.adj_list = { int(vert): adj_verts
                                  for vert, adj_verts
                                      in json.load(graph_file).items() }
            self.print_adj_list()
            self.adj_mat = self.make_adj_mat()
            self.print_adj_mat()

    def make_adj_mat(self):
        adj_mat = [ [0] * len(self.adj_list) for _ in self.adj_list ]
        for vert in self.adj_list:
            for adj_vert in self.adj_list[vert]:
                adj_mat[vert][adj_vert] = 1
        return adj_mat

    def print_adj_list(self):
        print('Adj list:')
        for vert in self.adj_list:
            print('%s : %s' % (vert, self.adj_list[vert]))

    def print_adj_mat(self):
        print('Adj mat:')
        for row in self.adj_mat:
            print(row)

    def dfs():
        pass

    def bfs():
        pass

    def dij():
        pass


graph_file_path = 'g1.json'
g = Graph(graph_file_path)
