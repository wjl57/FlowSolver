# from colorama import init as colorama_init
from FlowSolver.GridPuzzle import GridPuzzle

# colorama_init(True)
x_dim, y_dim, initial_locations = GridPuzzle.read_puzzle('Puzzles/RegularPack/6x6_1')
puzzle = GridPuzzle(x_dim, y_dim, initial_locations)
puzzle.print_nodes()
puzzle.print_char_array()
