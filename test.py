import random
import search
import utils

# a)
def make_rand_StagePuzzle():
    puzzleTurple = randomTurple()
    puzzle = search.StagePuzzle(puzzleTurple)
    while(not (puzzle.check_solvability(puzzleTurple))):
        puzzleTurple = randomTurple()
        puzzle = search.StagePuzzle(puzzleTurple)
    return puzzle
    
def randomTurple():
    orderList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    randomList = []
    for x in range(10):
        num = random.choice(orderList)
        randomList.append(num)
        orderList.remove(num)
    return tuple(randomList)

# b)
def display(state):
    print("  " + printState(state[0]) + " " + printState(state[1]))
    for i in range (2, 10):
        print(printState(state[i]) + " ", end = "")
        if i == 5:
            print("")
    print("")
         

def printState(num):
    if num == 0:
        return "*"
    else:
        return str(num)

puzzle = make_rand_StagePuzzle()
display(puzzle.initial)
