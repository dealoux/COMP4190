####################################
# Enums
####################################

class AnsiColors:
    GRAY = "\033[90m"
    RED = '\033[91m'
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    RESET = "\033[0m"
# AnsiColors end

class NodeStates:
    BULB = "b"
    WALL = "W"
    WALL0 = "0"
    WALL1 = "1"
    WALL2 = "2"
    WALL3 = "3"
    WALL4 = "4"
    EMPTY = "_"
# NodeStates end

class OverallStates:
    INVALID = 0
    VALID = 1
    COMPLETE = 2
    CANNOT_FINISH = 3
# OverallStates end

class HeuristicMode:
    NONE = 0
    MOST_CONSTRAINED = 1
    MOST_CONSTRAINING = 2
    HYBRID = 3
# HeuristicMode end

####################################
# Globals
####################################
MAX_SEARCH_ITERATIONS = 100000
HEURISTIC_MODE = HeuristicMode.MOST_CONSTRAINED
USE_COLOR_PRINT = True # Disable if terminal doesn't support ANSI escape codes (e.g. prints gibberish)

####################################
# Utility Functions
####################################
# ansi = string: from AnsiColors class
def colorPrint(ansi, *args, end=None, sep=" "):
    if USE_COLOR_PRINT:
        print(ansi, end="")
        print(*args, end="", sep=sep)
        print(AnsiColors.RESET, end="")
        print(end=end)
    else:
        print(*args, end=end)
# colorPrint end