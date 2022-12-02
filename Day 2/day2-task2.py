import re
# Opponent will play
# A = Rock, B = Paper, C = Scissors
# The result I should get
# X = lose, Y = draw, Z = win

# Scores
# I pick Rock(X) = 1, Paper(Y) = 2, Scissors(Z) = 3
# plus
# Result of lose = 0, draw = 3, win = 6

with open ("Day 2/input.txt", "r", encoding="utf8") as inputfile:
    score = int()
    for line in inputfile.readlines():
        game = re.match(r"(\w)\s(\w)", line)
        # Match the opponent output first
        match game.group(1):
            case "A":
                match game.group(2):
                    case "X":
                        score += 3
                    case "Y":
                        score += 4
                    case "Z":
                        score += 8
            case "B":
                match game.group(2):
                    case "X":
                        score += 1
                    case "Y":
                        score += 5
                    case "Z":
                        score += 9
            case "C":
                match game.group(2):
                    case "X":
                        score += 2
                    case "Y":
                        score += 6
                    case "Z":
                        score += 7

print(score)
