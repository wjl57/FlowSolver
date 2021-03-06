from enum import Enum


class NodeTypes(Enum):
    # Any node which does not currently belong to a color
    EMPTY = 0
    # The actual source for a color
    SOURCE = 1
    # The actual sink for a color
    SINK = 2
    # The last node for a particular flow from the source
    CURRENT_SOURCE = 3,
    # The first node for a particular flow to the sink
    CURRENT_SINK = 4,
    # Any node which is part of a flow from the source and is not the CURRENT_SOURCE
    FLOW_FROM_SOURCE = 5
    # Any node which is part of a flow from the source and is not the CURRENT_SOURCE
    FLOW_TO_SINK = 6
    # Any node which is part of a completed flow
    COMPLETED_FLOW = 7

    @staticmethod
    def get_node_shape(node_type):
        if node_type == NodeTypes.EMPTY:
            return "."
        elif node_type == NodeTypes.SOURCE:
            return "O"
        elif node_type == NodeTypes.SINK:
            return "X"
        elif node_type == NodeTypes.CURRENT_SOURCE:
            return "o"
        elif node_type == NodeTypes.CURRENT_SINK:
            return "x"
        elif node_type == NodeTypes.COMPLETED_FLOW:
            return "ø"
        return "*"

