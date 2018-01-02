from FlowSolver.Node import Node
from FlowSolver.Point import Point


class GridPuzzle:
    def __init__(self, x_dim, y_dim, initial_flows):
        self.x_dim = x_dim
        self.y_dim = y_dim
        self.puzzle = {}
        for x in range(0, x_dim):
            for y in range(0, y_dim):
                node_id = self.x_y_to_node_id(x, y)
                self.puzzle[node_id] = Node(node_id)

        # Add vertical neighbors
        for x in range(0, x_dim):
            for y in range(0, y_dim - 1):
                node_id = self.x_y_to_node_id(x, y)
                north_node_id = self.x_y_to_node_id(x, y+1)
                self.add_neighbors(node_id, north_node_id)

        # Add horizontal neighbors
        for y in range(0, y_dim):
            for x in range(0, x_dim - 1):
                node_id = self.x_y_to_node_id(x, y)
                east_node_id = self.x_y_to_node_id(x+1, y)
                self.add_neighbors(node_id, east_node_id)

        # Add initial flows
        for flow in initial_flows:
            node_id_1 = self.x_y_to_node_id(flow.x_1, flow.y_1)
            node_id_2 = self.x_y_to_node_id(flow.x_2, flow.y_2)
            node_1 = self.puzzle[node_id_1]
            node_2 = self.puzzle[node_id_2]
            node_1.add_point(flow.color, True)
            node_2.add_point(flow.color, True)

    def node_id_to_x_y(self, node_id):
        y = int(node_id / self.x_dim)
        x = node_id % self.x_dim
        return x, y

    def x_y_to_node_id(self, x, y):
        return x + y*self.x_dim

    def add_neighbors(self, node_id_1, node_id_2):
        self.puzzle[node_id_1].add_neighbor(node_id_2)
        self.puzzle[node_id_2].add_neighbor(node_id_1)

    def print_nodes(self):
        for node in self.puzzle.values():
            print(node)

    def print_char_array(self):
        for y in range(self.y_dim-1, -1, -1):
            for x in range(0, self.x_dim):
                node_id = self.x_y_to_node_id(x, y)
                node = self.puzzle[node_id]
                if node.color is None:
                    print("*6", end="")
                else:
                    print(node.color, end="")
            print()


class InitialFlows:
    def __init__(self, color, coord_1, coord_2):
        self.color = color
        self.x_1 = coord_1[0]
        self.y_1 = coord_1[1]
        self.x_2 = coord_2[0]
        self.y_2 = coord_2[1]

