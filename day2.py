
rock = "Rock"
paper = "Paper"
scissors = "Scissors"

play = {
    "A": rock,
    "B": paper,
    "C": scissors,
    "X": rock,
    "Y": paper,
    "Z": scissors,
}

score = {
    rock: 1,
    paper: 2,
    scissors: 3,
}

wins = {
    rock: scissors,
    paper: rock,
    scissors: paper,
}

loses = {
    scissors: rock,
    rock: paper,
    paper: scissors,
}

outcomes = {
    "X": "lose",
    "Y": "draw",
    "Z": "win",
}


def match(plays):
    player, elf = plays
    shape_score = score[player]
    rank_score = 0
    if player == elf:
        rank_score = 3
    if wins[player] == elf:
        rank_score = 6

    return shape_score + rank_score


def rigged(game):
    elf, outcome = game
    if outcome == "draw":
        return match([elf, elf])
    if outcome == "lose":
        return match([wins[elf], elf])
    return match([loses[elf], elf])


def part1():
    text = open("day2.txt", "r")
    games = []
    for line in text:
        p2, p1 = line.strip().split(" ")
        games.append([play[p1], play[p2]])

    scores = map(match, games)
    print(sum(scores))


def part2():
    text = open("day2.txt", "r")
    games = []
    for line in text:
        p2, result = line.strip().split(" ")
        games.append([play[p2], outcomes[result]])

    scores = map(rigged, games)
    print(sum(scores))


if __name__ == '__main__':
    part2()



