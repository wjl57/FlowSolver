from FlowSolver.NodeTypes import NodeTypes


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.neighbor_ids = set()
        self.color = None
        self.node_type = NodeTypes.EMPTY

    def add_neighbor(self, neighbor_id):
        self.neighbor_ids.add(neighbor_id)

    def modify_node(self, color, node_type):
        self.color = color
        self.node_type = node_type

    def __str__(self):
        return str(self.node_id) + " " + str(self.color) + ": " + str(self.neighbor_ids)
