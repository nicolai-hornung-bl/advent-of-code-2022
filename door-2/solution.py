from enum import Enum
from functools import total_ordering


class result(Enum):
    LOSS = 0
    DRAW = 3
    WIN = 6

class rps(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    def eval(self, other):
        order = {
            rps.ROCK: {
                rps.SCISSORS: result.WIN.value,
                rps.ROCK: result.DRAW.value,
                rps.PAPER: result.LOSS.value
            },
            rps.PAPER: {
                rps.ROCK: result.WIN.value,
                rps.PAPER: result.DRAW.value,
                rps.SCISSORS: result.LOSS.value
            },
            rps.SCISSORS: {
                rps.PAPER: result.WIN.value,
                rps.SCISSORS: result.DRAW.value,
                rps.ROCK: result.LOSS.value
            }
        }
        return self.value + order[self][other]

    def req(self, target_result):
        order = {
            rps.ROCK: {
                result.WIN: rps.PAPER,
                result.DRAW: rps.ROCK,
                result.LOSS: rps.SCISSORS
            },
            rps.PAPER: {
                result.WIN: rps.SCISSORS,
                result.DRAW: rps.PAPER,
                result.LOSS: rps.ROCK
            },
            rps.SCISSORS: {
                result.WIN: rps.ROCK,
                result.DRAW: rps.SCISSORS,
                result.LOSS: rps.PAPER
            }
        }
        return order[self][target_result]



opponent_map = {
        "A": rps.ROCK,
        "B": rps.PAPER,
        "C": rps.SCISSORS
}
player_map = {
    "X": rps.ROCK,
    "Y": rps.PAPER,
    "Z": rps.SCISSORS
}
result_map = {
    "X": result.LOSS,
    "Y": result.DRAW,
    "Z": result.WIN
}

def eval1(input):
    opponent_shape = opponent_map[input.split(" ")[0]]
    player_shape = player_map[input.split(" ")[1]]
    return rps.eval(player_shape, opponent_shape)

def eval2(input):
    opponent_shape = opponent_map[input.split(" ")[0]]
    target_result = result_map[input.split(" ")[1]]
    return rps.eval(opponent_shape.req(target_result), opponent_shape)    



with open('door-2/input.txt', 'r') as input:
    sum1 = 0
    sum2 = 0
    for line in input:
        sum1 += eval1(line.strip())
        sum2 += eval2(line.strip())
    input.close
    
print(sum1)
print(sum2)
