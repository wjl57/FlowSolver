from FlowSolver.GridPuzzle import GridPuzzle, InitialFlows

puzzle = GridPuzzle(5, 5,
                    [
                        InitialFlows('G', (0, 0), (4, 4)),
                        InitialFlows('B', (1, 0), (3, 1)),
                        InitialFlows('Y', (2, 0), (2, 2)),
                        InitialFlows('R', (0, 3), (3, 4))
                    ])

puzzle.print_nodes()
puzzle.print_char_array()
