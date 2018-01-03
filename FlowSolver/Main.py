import sys

from FlowSolver.GridPuzzle import GridPuzzle

x_dim, y_dim, initial_locations = GridPuzzle.read_puzzle('Puzzles/RegularPack/5x5_1')
puzzle = GridPuzzle(x_dim, y_dim, initial_locations)
# puzzle.print_nodes()
puzzle.print_puzzle()
puzzle.solve_next_step()
# puzzle.print_nodes()
puzzle.print_puzzle()
puzzle.solve_next_step()
puzzle.print_puzzle()
puzzle.solve_next_step()
puzzle.print_puzzle()
puzzle.finish_color('Y')
puzzle.print_puzzle()