import re
# Opponent will play
# A = Rock, B = Paper, C = Scissors
# I "Should" play
# X = Rock, Y = Paper, Z = Scissors

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
                        score += 4
                    case "Y":
                        score += 8
                    case "Z":
                        score += 3
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
                        score += 7
                    case "Y":
                        score += 2
                    case "Z":
                        score += 6

print(score)
