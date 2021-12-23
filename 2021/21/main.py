import sys
import functools

sys.setrecursionlimit(10**7)

def deterministic_dice(turn, players, scores):
    if scores[0] >= 1000 or scores[1] >= 1000:
        return min(scores) * turn * 3
    
    num = turn % 2
    roll = (turn * 9) + (1 + 2 + 3)
    players[num] = (players[num] + roll - 1) % 10 + 1
    scores[num] += players[num]
    return deterministic_dice(turn + 1, players, scores)

players = [4, 9]
scores = [0, 0]
print("q1", deterministic_dice(0, players, scores))

rolls = {
    3: 1,
    4: 3,
    5: 6,
    6: 7,
    7: 6,
    8: 3,
    9: 1
}

@functools.lru_cache(maxsize=None)
def dirac_multiverse(turn, player0, player1, score0, score1):
    players = [player0, player1]
    scores = [score0, score1]

    if scores[0] >= 21:
        return [1, 0]
    elif scores[1] >= 21:
        return [0, 1]

    win_counts = [0, 0]
    num = turn % 2
    for roll, times in rolls.items():
        players[num] = (players[num] + roll -1) % 10 + 1
        scores[num] += players[num]
        results = dirac_multiverse(turn + 1, players[0], players[1], scores[0], scores[1])
        win_counts[0] += times * results[0]
        win_counts[1] += times * results[1]
        scores[num] -= players[num]
        players[num] = (players[num] - roll -1) % 10 + 1

    return win_counts

players = [4, 9]
scores = [0, 0]
win_counts = dirac_multiverse(0, players[0], players[1], scores[0], scores[1])
print("q2", max(win_counts))