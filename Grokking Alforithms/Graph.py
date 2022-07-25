from turtle import st


class Graph:
    def __init__(self, edges=None):
        self.graph_dict = {}

        # self.edges = edges
        for start, end in edges:
            self.graph_dict[start] = self.graph_dict.get(start, [])+[end]

        print([print(f"{item}:{self.graph_dict[item]}")
              for item in self.graph_dict.keys()])

    def getPathes(self, start, end, path=[]):
        pathes = []

        def rec(start, end, path=[]):
            path = path+[start]
            if start == end:
                pathes.append(path)
            if start not in self.graph_dict:
                return []
            for node in self.graph_dict[start]:
                if node not in path:
                    rec(node, end, path)

            return pathes

        return rec(start, end, path=[])

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
            if start not in self.graph_dict:
                return
            for node in self.graph_dict[start]:
                if node not in path:
                    rec(node, end,  mx, path)

        rec(start, end, mx, path=[])  # calling the fun

        # sort and return the smallest len
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
    # print(pathes)
    print(gh1.getShortesPath("Mumbai", "New York"))
