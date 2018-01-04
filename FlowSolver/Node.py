from FlowSolver.NodeTypes import NodeTypes


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.neighbor_ids = set()
        self.original_neighbor_ids = set()
        self.color = None
        self.node_type = NodeTypes.EMPTY

    def add_neighbor(self, neighbor_id):
        self.neighbor_ids.add(neighbor_id)
        self.original_neighbor_ids.add(neighbor_id)

    def remove_neighbor(self, neighbor_id):
        if neighbor_id in self.neighbor_ids:
            self.neighbor_ids.remove(neighbor_id)

    def clear_neighbors(self):
        self.neighbor_ids.clear()

    def modify_node(self, node_type, color=None):
        # Don't change immutable node types
        if self.node_type is not NodeTypes.SOURCE and self.node_type is not NodeTypes.SINK:
            self.node_type = node_type
        if color is not None and self.color is None:
            self.color = color

    def __str__(self):
        return str(self.node_id) + " " + str(self.color) + ": " + str(self.neighbor_ids)
