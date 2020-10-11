import random
import search
import utils
import time

# a)
def make_rand_StagePuzzle():
    puzzleTurple = random_turple()
    puzzle = search.StagePuzzle(puzzleTurple)
    while(not (puzzle.check_solvability(puzzleTurple))):
        puzzleTurple = random_turple()
        puzzle = search.StagePuzzle(puzzleTurple)
    return puzzle
    
def random_turple():
    orderList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    randomList = []
    for x in range(10):
        num = random.choice(orderList)
        randomList.append(num)
        orderList.remove(num)
    return tuple(randomList)

# b)
def display(state):
    print("  " + star_or_number(state[0]) + " " + star_or_number(state[1]))
    for i in range (2, 10):
        print(star_or_number(state[i]) + " ", end = "")
        if i == 5:
            print("")
    print("")
         

def star_or_number(num):
    if num == 0:
        return "*"
    else:
        return str(num)

# c)
# Modified version from textbook's code ()
def manhattan(node):
    state = node.state
    index_goal = {0: [2, 3], 1: [0, 1], 2: [0, 2], 3: [1, 0], 4: [1, 1], 5: [1, 2], 6: [1, 3], 7: [2, 0], 8: [2, 1], 9: [2, 2]}
    index_state = {}
    index = [[0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [1, 3], [2, 0], [2, 1], [2, 2], [2, 3]]

    for i in range(len(state)):
        index_state[state[i]] = index[i]

    distance = 0

    for i in range(10):
         for j in range(2):
            distance += abs(index_goal[i][j] - index_state[i][j])

    return distance


def time_default(puzzle):
    print("Default Heuristic")
    start_time = time.time()
    search.astar_search(puzzle, puzzle.h, True)
    end_time = time.time()
    print("Default time: " + str(end_time-start_time))

def time_manhattan(puzzle):
    print("Manhattan Heuristic")
    start_time = time.time()
    search.astar_search(puzzle, manhattan, True)
    end_time = time.time()
    print("Manhattan time: " + str(end_time-start_time))
    
def time_max(puzzle):
    print("Max Heuristic")
    start_time = time.time()
    search.astar_search(puzzle, max(puzzle.h, manhattan), True)
    end_time = time.time()
    print("Max time: " + str(end_time-start_time))

puzzle = make_rand_StagePuzzle()
display(puzzle.initial)
time_default(puzzle)

