
class Weighted_Graph:
    def __init__(self, edges=None):
        self.graph = {}  # Node1 :{ neighbour1:cost1 , neighbour2:cost2 }
        # filling the graph dic with the data
        for Node, neighbour in edges:
            # if the Node dosnt exist yet in the graph , then anitialize its
            if not self.graph.get(Node, False):
                self.graph[Node] = {}
            # add the neighbour dic to the "value" of the Node
            self.graph[Node].update(neighbour)

    def __str__(self):
        return str([f"{item}:{self.graph[item]}"
                    for item in self.graph])

    def find_lowest_cost_node(self, costs):
        if costs:
            lowest = min(costs, key=costs.get)
            # lowest = sorted(costs, key=costs.get)[0]
            # for node in self.graph[lowest]:
            #     if not costs.get(node, False):
            #         costs[node] = legth+self.graph[lowest][node]

            return lowest
        return None  # return None if costs is empty

    def Dijkstra_Path(self, start, end):

        neighbours = self.graph[start]
        costs = {}
        costs.update(neighbours)
        parents = {k: start for k in neighbours}
        node = self.find_lowest_cost_node(costs)
        while node:
            cur_cost = costs[node]
            neighbours = self.graph.get(node, {})
            for n in neighbours:
                new_Cost = cur_cost+neighbours[n]
                if not costs.get(n, False):
                    costs[n] = new_Cost
                elif costs[n] > new_Cost:
                    costs[n] = new_Cost
                    parents[n] = node
            del costs[node]
            node = self.find_lowest_cost_node(costs)

            # printing the path
        path = []
        while end != start and parents:
            path.append(end)
            end = parents[end]
        path.append(start)
        path.reverse()
        print(path)


if __name__ == '__main__':
    routes1 = [
        ("Mumbai", {"Paris": 4}),
        ("Mumbai", {"Dubai": 6}),
        ("Paris", {"Dubai": 7}),
        ("Paris", {"New York": 8}),
        ("Dubai", {"New York": 2}),
        ("New York", {"Toronto": 1}),
    ]

    routes2 = [
        ("start", {"A": 6}),  # A
        ("start", {"B": 2}),  # 6 /  |   \ 1
        ("B", {"A": 3}),  # strat  3|   fin
        ("B", {"fin": 8}),  # 5 \ |   / 5
        ("A", {"fin": 1}),  # B
    ]
    # Wgh = Weighted_Graph(routes1)
    # print(Wgh)
    # Wgh.Dijkstra_Path("Mumbai", "New York")
    Wgh = Weighted_Graph(routes2)
    print(Wgh)
    Wgh.Dijkstra_Path("start", "fin")
