from collections import deque


class Graph:
    def __init__(self, edges=None):
        self.graph = {}

        # self.edges = edges
        # filling the graph dic with the data
        for node, end in edges:
            self.graph[node] = self.graph.get(node, [])+[end]

        # print([print(f"{item}:{self.graph[item]}")
        #       for item in self.graph.keys()])

    def __str__(self):

        return str([f"{item}:{self.graph[item]}"
                    for item in self.graph])

    def getPathes(self, start, end, path=[]):
        pathes = []

        def rec(start, end, path=[]):
            path = path+[start]
            if start == end:
                pathes.append(path)
            if start not in self.graph:
                return []
            for node in self.graph[start]:
                if node not in path:
                    rec(node, end, path)

            return pathes

        return rec(start, end, path=[])

    def breadth_frist_search(self, start, end):  # search the neighbours frist
        search_queue = deque()
        searched = []
        search_queue += [start]
        while search_queue:
            position = search_queue.popleft()
            if not position in searched:
                if position == end:
                    return True
                searched.append(position)
                search_queue += self.graph.get(position, [])
        return False

    def getShortesPath(self, start, end, path=[]):
        mx = float("infinity")
        pathes = []

        def rec(start, end, mx, path=[]):
            path = path+[start]
            path_len = len(path)
            if path_len > mx:
                return
            if start == end:
                pathes.append(path)
                mx = path_len
                return
            if start not in self.graph:
                return
            for node in self.graph[start]:
                if node not in path:
                    rec(node, end,  mx, path)

        rec(start, end, mx, path=[])  # calling the fun

        # sort and return the smallest len
        # if pathes empty return None
        return sorted(pathes, key=lambda x: len(x))[0] if pathes else None


if __name__ == '__main__':
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]
    gh1 = Graph(routes)
    # pathes = gh1.getPathes("Mumbai", "New York")
    print(gh1)
    print(gh1.breadth_frist_search("Paris", "Toronto"))
