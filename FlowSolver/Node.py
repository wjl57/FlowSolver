class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.neighbor_ids = set()
        self.color = None
        self.is_endpoint = False

    def add_neighbor(self, neighbor_id):
        self.neighbor_ids.add(neighbor_id)

    def add_point(self, color, is_endpoint):
        self.color = color
        self.is_endpoint = is_endpoint

    def __str__(self):
        return str(self.node_id) + " " + str(self.color) + ": " + str(self.neighbor_ids)
