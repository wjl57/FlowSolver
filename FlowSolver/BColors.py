class BColors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    YELLOW = '\033[93m'
    MAGENTA = '\033[95m'
    GREY = '\033[90m'
    BLACK = '\033[90m'
    DEFAULT = '\033[99m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @staticmethod
    def get_terminal_color(color):
        if color == 'R':
            return BColors.RED
        elif color == 'B':
            return BColors.BLUE
        elif color == 'G':
            return BColors.GREEN
        elif color == 'Y':
            return BColors.YELLOW
        elif color == 'M':
            return BColors.MAGENTA
        elif color == 'C':
            return BColors.CYAN
        elif color == 'W':
            return BColors.WHITE
        return BColors.DEFAULT
