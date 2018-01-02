class Flow:
    """

    """
    def __init__(self, color, node_id_1, node_id_2):
        self.color = color
        self.start_nodes = [node_id_1]
        self.end_nodes = [node_id_2]