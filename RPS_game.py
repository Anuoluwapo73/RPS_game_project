import random

def play(player1, player2, num_games=1000, verbose=False):
    p1_score = 0
    p2_score = 0
    p1_prev = ""
    p2_prev = ""
    p1_history = []
    p2_history = []

    for _ in range(num_games):
        move1 = player1(p2_prev, p2_history)
        move2 = player2(p1_prev, p1_history)

        if verbose:
            print(f"You played {move1}, Opponent played {move2}")

        if beats(move1, move2):
            p1_score += 1
        elif beats(move2, move1):
            p2_score += 1

        p1_prev = move1
        p2_prev = move2
        p1_history.append(move1)
        p2_history.append(move2)

    if verbose:
        print(f"Final results: You won {p1_score / num_games * 100}% of the games")

    return p1_score / num_games

def beats(one, two):
    return (one == "R" and two == "S") or \
           (one == "S" and two == "P") or \
           (one == "P" and two == "R")

def quincy(prev_play, opponent_history=[]):
    return "R"

def abbey(prev_play, opponent_history=[]):
    if not prev_play:
        opponent_history.clear()
    opponent_history.append(prev_play)
    guess = opponent_history[-1] if opponent_history[-1] else "R"
    return {"R": "P", "P": "S", "S": "R"}[guess]

def kris(prev_play, opponent_history=[]):
    return random.choice(["R", "P", "S"])

def mrugesh(prev_play, opponent_history=[]):
    if not prev_play:
        opponent_history.clear()
    opponent_history.append(prev_play)
    guess = most_common(opponent_history[-5:])
    return {"R": "P", "P": "S", "S": "R"}[guess]

def most_common(history):
    return max(set(history), key=history.count)
