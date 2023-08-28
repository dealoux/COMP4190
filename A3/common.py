####################################
# Enums
####################################

from re import X


class State:
    x = 0
    y = 0
# State end

class Action:
    EAST = 1
    NORTH = 2
    WEST = 3
    SOUTH = 4

    NONE = 0 # no action
    EXIT = -1 # exit action
# Action end

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