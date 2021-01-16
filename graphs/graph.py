from math import inf
from copy import deepcopy

import yaml

# implemented by pseudocode from wiki

# Directed graph
class Graph:

    def __init__(self, graph_file_path):
        self.load_graph(graph_file_path)
        self.print_adj_list()

    def add_new_vert(self, adj_list, vert):
        if vert not in adj_list:
            adj_list[vert] = {}

    def load_adj_list(self, input_adj_list):
        '''
            - adding missed verts in input_adj_list keys
              (for directed graphs with sinks, which may be not presented
              in the input_adj_list keys)
        '''
        adj_list = {}
        for vert in input_adj_list:
            self.add_new_vert(adj_list, vert)
            for adj_vert, length in input_adj_list[vert].items():
                self.add_new_vert(adj_list, adj_vert)
                adj_list[vert][adj_vert] = length
        return adj_list

    def load_graph(self, graph_file_path):
        # reading graph file
        graph = yaml.safe_load(open(graph_file_path, 'r'))
        # load graph data
        self.adj_list = self.load_adj_list(graph['data'])
        print('Graph loading success!')

    def print_adj_list(self):
        print('Adj list:')
        for vert in self.adj_list:
            print('%s : %s' % (vert, self.adj_list[vert]))

    # NOTE: recursive implementation
    def dfs(self, start_vert):
        visited = set()
        print('DFS:')
        self.__dfs(start_vert, visited)
        print()

    def __dfs(self, vert, visited):
        '''Depth-first-search algorithm'''

        print(vert, end=' ')
        visited.add(vert)
        for adj_vert in self.adj_list[vert]:
            if adj_vert not in visited:
                self.__dfs(adj_vert, visited)

    def bfs(self, start_vert):
        '''Breadth-first search algorithm'''

        queue = [ start_vert ]
        visited = set([ start_vert ])
        print('BFS:')
        while queue:
            # print(queue)
            vert = queue.pop(0)
            print(vert, end=' ')
            for adj_vert in self.adj_list[vert]:
                if adj_vert not in visited:
                    queue.append(adj_vert)
                    visited.add(adj_vert)
        print()

    def pop_closest(self, target_verts, dists):
        closest_vert = None
        min_dist = inf
        for vert in target_verts:
            if dists[vert] < min_dist:
                min_dist = dists[vert]
                closest_vert = vert
        target_verts.discard(closest_vert)
        return closest_vert, min_dist

    # TODO: implement with priority queue
    def dij(self, start_vert):
        '''Dijkstra algorithm'''

        print('Dijkstra:')
        # initializing
        target_verts, dists, prevs = set(), {}, {}
        for vert in self.adj_list:
            dists[vert] = inf
            prevs[vert] = None
            target_verts.add(vert)
        
        # start from spec vert
        dists[start_vert] = 0
        while target_verts:
            closest_vert, dist = self.pop_closest(target_verts, dists)
            # targets exist, but all have inf distance
            if closest_vert is None:
                print('Note: graph has unreachable vertices: %s' % target_verts)
                break
            print('-' * 10)
            print('closest: %s (%s)' % (closest_vert, dist))
            # relaxation (weight updating)
            for adj_vert, length in self.adj_list[closest_vert].items():
                if adj_vert in target_verts:
                    new_dist = dists[closest_vert] + length
                    print('dist [%s]: %s' % (adj_vert, new_dist))
                    if new_dist < dists[adj_vert]:
                        print('update [%s]: %s -> %s' % (adj_vert, dists[adj_vert], new_dist))
                        dists[adj_vert] = new_dist
                        prevs[adj_vert] = closest_vert
        print('Dists: %s' % dists)
        print('Prevs: %s' % prevs)
        return dists, prevs

    def restore_path(self, prevs, target_vert):
        print('Restored path from vertex "%s":' % target_vert)
        print(target_vert, end=' ')
        while prevs[target_vert]:
            target_vert = prevs[target_vert]
            print(target_vert, end=' ')
        print()

    def is_source(self, target_vert, adj_list):
        for vert in adj_list:
            for adj_vert in adj_list[vert]:
                if adj_vert == target_vert:
                    return False
        return True

    # NOTE: own implementation (far not optimal)
    def top_sort(self):
        '''
            Topological sort
            (sorting with smallest-numbered available vertex first in level)
        '''

        print('Topological sort:')
        # making deep copy of initial adj_list
        # for safe links removing
        adj_list = deepcopy(self.adj_list)
        # list for storing result
        sorted_seq = []

        layer_ind = 0
        while True:
            # finding and sorting available source verts
            sources = sorted([ vert for vert in adj_list if self.is_source(vert, adj_list) ])

            # if no one source vert
            if not sources:
                break

            # marking sources with layer ind and saving
            sorted_seq.extend(map(lambda source: (source, layer_ind), sources))
            
            # removing all sources
            for source in sources:
                adj_list.pop(source)
            
            # inc layer ind
            layer_ind += 1
        
        # result
        if adj_list:
            print('Error: cycle exists!')
        print(sorted_seq)
