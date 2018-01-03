class FColors:
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
    def get_fg_color(color):
        if color == 'R':
            return FColors.RED
        elif color == 'B':
            return FColors.BLUE
        elif color == 'G':
            return FColors.GREEN
        elif color == 'Y':
            return FColors.YELLOW
        elif color == 'M':
            return FColors.MAGENTA
        elif color == 'C':
            return FColors.CYAN
        elif color == 'W':
            return FColors.WHITE
        return FColors.DEFAULT


