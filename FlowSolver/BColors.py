class BColors:
    BLACK = '\033[40m'
    RED = '\033[41m'
    GREEN = '\033[42m'
    YELLOW = '\033[43m'
    BLUE = '\033[44m'
    MAGENTA = '\033[45m'
    CYAN = '\033[46m'
    WHITE = '\033[47m'
    ENDC = '\033[0m'

    @staticmethod
    def get_bg_color(color):
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
        return BColors.BLACK
