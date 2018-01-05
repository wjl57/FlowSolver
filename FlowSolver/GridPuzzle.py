import os
from collections import defaultdict
from time import sleep
import logging

from FlowSolver.FColors import FColors
from FlowSolver.Node import Node
from FlowSolver.NodeTypes import NodeTypes

logging.basicConfig(filename="test.log", level=logging.DEBUG)


class GridPuzzle:
    def __init__(self, x_dim, y_dim, initial_locations):
        self.x_dim = x_dim
        self.y_dim = y_dim
        self.puzzle = {}
        self.current_source_node_ids = {}
        self.current_sink_node_ids = {}
        self.colors = []
        self.color_index = -1
        self.current_color = None
        # These settings can be toggled
        self.debug = True
        self.sleep_time = 0.1

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

        # Add initial locations (Dictionary of Color -> [NodeId])
        for color, node_ids in initial_locations.items():
            # Add all colors
            self.colors.append(color)

            # Add all source nodes
            source_node_id = node_ids[0]
            source_node = self.puzzle[source_node_id]
            source_node.modify_node(NodeTypes.SOURCE, color)
            self.remove_incoming_neighbors(source_node_id)
            self.current_source_node_ids[color] = source_node_id

            # Add all sink nodes
            sink_node_id = node_ids[1]
            sink_node = self.puzzle[sink_node_id]
            sink_node.modify_node(NodeTypes.SINK, color)
            sink_node.clear_neighbors()
            self.current_sink_node_ids[color] = sink_node_id

        # Set an initial color
        self.next_color()

    def next_color(self):
        if not self.colors:
            return
        self.color_index = (self.color_index + 1) % len(self.colors)
        self.current_color = self.colors[self.color_index]
        logging.debug("Checking color: " + self.current_color)

    def solve_puzzle(self):
        print("Provided puzzle:")
        self.print_puzzle()
        count = 0
        while self.colors:
            count += 1
            made_progress = self.solve_next_step()
            if made_progress:
                self.print_puzzle_debug()
                finished_flow = self.try_finish_flow(self.current_color)
                if finished_flow:
                    self.print_puzzle_debug()
                    self.next_color()
            else:
                self.next_color()
        print("Done!")
        self.print_puzzle()
        logging.info("Solving the puzzle took " + str(count) + " steps")

    def solve_next_step(self):
        node_id = self.current_source_node_ids[self.current_color]
        # Find and make a forced move
        next_node_id = self.find_forced_move(node_id)
        if next_node_id is not None:
            self.update_current_source(node_id, next_node_id)
            return True
        return False

    def try_finish_flow(self, color):
        # Finish a flow if possible
        if self.find_finished_flow(color):
            self.finish_flow(color)
            return True
        return False

    def remove_incoming_neighbors(self, node_id):
        for neighbor_node_id in self.puzzle[node_id].original_neighbor_ids:
            neighbor_node = self.puzzle[neighbor_node_id]
            neighbor_node.remove_neighbor(node_id)

    def find_forced_move(self, node_id):
        node = self.puzzle[node_id]
        # If there is only one node to move to
        if len(node.neighbor_ids) == 1:
            forced_neighbor_id = node.neighbor_ids.pop()
            return forced_neighbor_id
        # If a neighbor is adjacent to a single source and only has one free neighbor
        for neighbor_id in node.neighbor_ids:
            neighbor_node = self.puzzle[neighbor_id]
            if len(neighbor_node.neighbor_ids) == 1:
                adjacent_sources = set(self.current_source_node_ids.values()) & neighbor_node.original_neighbor_ids
                if len(adjacent_sources) == 1:
                    return neighbor_id
        return None

    def find_finished_flow(self, color):
        node = self.puzzle[self.current_source_node_ids[color]]
        sink_node_id = self.current_sink_node_ids[color]
        return sink_node_id in node.neighbor_ids

    def finish_flow(self, color):
        self.colors.remove(color)
        logging.info("Finished flow for " + color + ". Remaining: " + str(self.colors))
        self.remove_incoming_neighbors(self.current_sink_node_ids[color])
        # TODO: This is not remotely efficient
        for flow_node in [n for n in self.puzzle.values() if n.color == color]:
            flow_node.modify_node(NodeTypes.COMPLETED_FLOW)

    def update_current_source(self, old_source_id, new_source_id):
        old_source_node = self.puzzle[old_source_id]
        new_source_node = self.puzzle[new_source_id]
        color = old_source_node.color
        new_source_node.modify_node(NodeTypes.CURRENT_SOURCE, color)
        old_source_node.modify_node(NodeTypes.FLOW_FROM_SOURCE)
        self.remove_incoming_neighbors(new_source_id)
        old_source_node.clear_neighbors()
        self.current_source_node_ids[color] = new_source_id
        logging.info("Updated " + color + " source from " + str(old_source_id) + " to " + str(new_source_id))

    def node_id_to_x_y(self, node_id):
        y = self.y_dim - 1 - int(node_id / self.x_dim)
        x = node_id % self.x_dim
        return x, y

    def x_y_to_node_id(self, x, y):
        return x + (self.y_dim - 1 - y)*self.x_dim

    def add_neighbors(self, node_id_1, node_id_2):
        self.puzzle[node_id_1].add_neighbor(node_id_2)
        self.puzzle[node_id_2].add_neighbor(node_id_1)

    def print_nodes(self):
        for node in self.puzzle.values():
            print(node)

    def print_puzzle_debug(self):
        if self.debug:
            self.print_puzzle()

    def print_puzzle(self):
        sleep(self.sleep_time)
        for y in range(self.y_dim-1, -1, -1):
            for x in range(0, self.x_dim):
                node_id = self.x_y_to_node_id(x, y)
                node = self.puzzle[node_id]
                node_shape = NodeTypes.get_node_shape(node.node_type)
                terminal_color = FColors.get_fg_color(node.color)
                print(terminal_color + node_shape + FColors.ENDC, end="", flush=True)
            print(flush=True)
        print(flush=True)

    @staticmethod
    def read_puzzle(relative_file_path):
        y_dim = 0
        initial_locations = defaultdict(list)
        absolute_file_path = os.path.join(os.path.dirname(__file__), relative_file_path)
        file = open(absolute_file_path)
        node_id = 0
        for line in file:
            if line.strip():
                y_dim += 1
            for c in line.strip():
                if c is not '.':
                    initial_locations[c].append(node_id)
                node_id += 1
        x_dim = int(node_id / y_dim)
        return x_dim, y_dim, initial_locations
