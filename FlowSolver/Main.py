import sys

from FlowSolver.GridPuzzle import GridPuzzle

x_dim, y_dim, initial_locations = GridPuzzle.read_puzzle('Puzzles/RegularPack/6x6_1')
puzzle = GridPuzzle(x_dim, y_dim, initial_locations)
puzzle.solve_puzzle()