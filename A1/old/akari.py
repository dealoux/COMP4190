class board:
    row = 0
    col = 0
    nodes = []

    def __init__(self, r, c):
        self.row = r
        self.col = c
        self.nodes = []

class akari_csp:
    def handleinput():
        filename = input("Please enter the input file: ")

        with open(filename, "r") as file:
            currPuzz = 0

            for line in file:
                if "Start" in line:
                    line = file.readline()
                
                    currBoard = board(int(line[0]), int(line[2]))
                    for i in range(currBoard.row):
                        r = file.readline()
                        r = r[:-1]
                        currBoard.nodes.append(r)

                elif "End" in line:
                    currPuzz += 1
                    print(f"Puzzle {currPuzz}")
                    print(currBoard.nodes)
                else:
                    continue