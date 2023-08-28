# birth_year = input('birth year: ')
# print(type(birth_year))
# age = 2022 - int(birth_year)
# print(type(age))
# print(age)


# first = 'John'
# last = "Smith"
# msg = f"{first} [{last}] is a programmer"
# print(msg)


# str = 'testing some shjt'
# print(len(str))
# print(str.upper())
# print(str.lower())
# print(str.title())
# print(str.find('sh'))
# print(str.replace('t', 'T'))
# print('shjt' in str)


# x = 10
# x //= 3
# print(x)


# is_hot = False
# is_cold = False
# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("It's a cold day")
#     print("Wear warm clothes")
# else:
#     print("It's a lovely day")
# print("Enjoy your day")


# price = 1000000
# has_good_credit = False
# has_high_income = True
# has_criminal_record = False

# if has_good_credit:
#     down_payment = .1 * price
# else:
#     down_payment = .2 * price
# print(f"Down payment: ${down_payment}")

# if (has_good_credit or has_high_income) and not has_criminal_record:
#     print("Eligible for loan")

# name = input('Please enter your name: ')
# nlen = len(name)
# if nlen < 3:
#     print("Name is too short, must be at least 3 characters")
# elif nlen > 50:
#     print("Name is too long, must be less than 50 characters")
# else:
#     print("Name looks good!")


# i = 1
# while i<= 5:
#     print("bruh " * i)
#     i += 1
# print("Done")


# for item in ["what", "the", "foot"]:
#     print(item)

# for item in range(5, 10, 2):
#     print(item)

# prices = [10, 20, 30]
# total = 0
# for price in prices:
#     total += price
# print(f"Total price is ${total}")


# for x in range(4):
#     for y in range(3):
#         print(f"({x}, {y})")

# x_counts = [5, 2, 5, 2, 2]
# for x_count in x_counts:
#     print("x" * x_count)


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(matrix[0][1])

# for row in matrix:
#     print(row)

# def handleinput():
#     filename = input("Please enter the input file: ")

#     with open(filename, "r") as file:
#         currPuzz = 0

#         for line in file:
#             if "Start" in line:
#                 line = file.readline()
                
#                 matrix = []
#                 for i in range(int(line[0])):
#                     row = file.readline()
#                     row = row[:-1]
#                     matrix.append(row)
#             elif "End" in line:
#                 currPuzz += 1
#                 print(f"Puzzle {currPuzz}")
#                 print(matrix[0][1])
#                 print(matrix)
#             else:
#                 continue


class board:
    row = 0
    col = 0
    nodes = []
    domains = []
    constraints = []
    wallPos = []

    def __init__(self, r, c):
        self.row = r
        self.col = c
        self.nodes = []
        self.domains = ["_", "b"]
        self.constraints = []
        wallPos = []

    def initDomain(self):
        maxDomain = 0

        for r in range(self.row):
            wallPosCol = []
            for c in range(self.col):
                if self.nodes[r][c] == "_":
                    continue

                wallPosCol.append(c)
                value = int(self.nodes[r][c])
                if value > maxDomain:
                    maxDomain = value
            self.wallPos.append(wallPosCol)
        
        newDomains = range(maxDomain)
        for d in newDomains:
            self.domains.append(d)

    # def initConstraints(self):
    #     for r in range(self.row-1):
    #         for c in range(self.col-1): 

    def checkLeft(self, pos):
        if pos[1] > 0:
            if self.nodes[pos[0]][pos[1] - 1] == "_":
                return True
            else:
                return False
        # If its out of index
        else:
            return False

    def checkRight(self, pos):
        if pos[1] + 1 < self.col:
            if self.nodes[pos[0]][pos[1] + 1] == "_":
                return True
            else:
                return False
        # If its out of index
        else:
            return False

    def checkTop(self, pos):
        if pos[0] > 0:
            if self.nodes[pos[0] - 1][pos[1]] == "_":
                return True
            else:
                return False
        # If its out of index
        else:
            return False

    def checkBottom(self, pos):
        if pos[0] + 1 < self.row:
            if self.nodes[pos[0] + 1][pos[1]] == "_":
                return True
            else:
                return False
        # If its out of index
        else:
            return False



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
                    currBoard.initDomain()

                elif "End" in line:
                    currPuzz += 1
                    print(f"Puzzle {currPuzz}")
                    print(currBoard.nodes[0][1] == 1)
                    print(currBoard.domains)
                    print(currBoard.nodes)
                else:
                    continue

handleinput()