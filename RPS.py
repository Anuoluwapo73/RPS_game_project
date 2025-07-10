def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)
    
    #count how many times opponent palyed R, P or S
    count_R = opponent_history.count("R")
    count_P = opponent_history.count("P")
    count_S = opponent_history.count("S")

    # predict the opponent's next move based on what they played most
    if count_R >= count_P and count_R >= count_S:
        prediction = "R"
    elif count_P >= count_R and count_P >= count_S:
        prediction = "P"
    else:
        prediction = "S"
        
    # return the move that beats the predicted move
    if prediction == "R":
        return "P" #paper beats rock
    elif prediction == "P":
        return "S" #scissors beats paper
    else:
        return "R" #rock beats scissors