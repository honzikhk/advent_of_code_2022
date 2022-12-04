"""
--- Part Two ---
The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated. The example above now goes like this:

In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also choose Rock. This gives you a score of 1 + 3 = 4.
In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.
Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.

Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?

Your puzzle answer was 13433.
"""

res = {
    "A Y": "win", "B Z": "win", "C X": "win",
    "A Z": "loss", "B X": "loss", "C Y": "loss",
    "A X": "draw", "B Y": "draw", "C Z": "draw"
    }

res2 = {
    "win_a": "A Y", "win_b": "B Z", "win_c": "C X",
    "lose_a": "A Z", "lose_b": "B X", "lose_c": "C Y",
    "draw_a": "A X", "draw_b": "B Y", "draw_c": "C Z"
    }

def change_result(round):
    phrase = str(round[0].lower())
    if round[2] == "X":     # i have to lose
        key = "lose_" + phrase
        return res2[key]

    elif round[2] == "Y":       # i have to draw
        key = "draw_" + phrase
        return res2[key]

    elif round[2] == "Z":       # i have to win
        key = "win_" + phrase
        return res2[key]


def calc_score(input):
    my_shape_score = {"X": 1, "Y": 2, "Z": 3}
    my_score = 0

    with open(input, "r") as file:
        data = file.readlines()

    for round in data:
        changed_round = change_result(round)
        result = res[changed_round[0:3]]
        score = my_shape_score[changed_round[2]]

        if result == "win":
            my_score += 6 + score

        elif result == "loss":
            my_score += score

        else:
            my_score += 3 + score
    return my_score


print(calc_score("day_2/2.1_day_input.sql"))