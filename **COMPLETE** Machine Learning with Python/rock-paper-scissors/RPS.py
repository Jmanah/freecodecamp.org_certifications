import random

def player(prev_play = "R", prev_me=["R"], stratagy={'RRRR':[0,0,0]}, mem=['RR','RR'] ):
    # print('\n')
    # print(stratagy)
    # Updates stratagy based upon opponents responces to a certain field
    field = "".join(mem)            # describes the two rounds before last
    if field not in stratagy:       # if new field is encountered new field is added to the stratagy
        stratagy[field] = [0,0,0]
    # incrament the responce count of a field based upon the opponents responce to a given field
    if prev_play == 'R':
        stratagy[field][0] += 1
    if prev_play == 'P':
        stratagy[field][1] += 1
    if prev_play == 'S':
        stratagy[field][2] += 1

    # deletes the round before the round before last and adds the last round to the list
    if prev_play != "":
        last_game = f"{prev_play}{prev_me[0]}"
    else:
        last_game = "X" # do not record first game as no data is available
    # update memory of last two games
    mem.pop(0)
    mem.append(last_game)

    # update field to describe the last two rounds
    field = "".join(mem)

    # selects a trump based upon the opponents behavioral history described in stratagy
    trump = ["P","S","R"]                                     # victory conditions if opponent selects ["R","P","S"] respectivly
    field = "".join(mem)                                      # update field to describe the last two rounds
    if field in stratagy:                                     # incase there is a tie for most likely responce from opponent, randomly select between the posibilities
        choices = []      
        for i in range(len(stratagy[field])):
            if stratagy[field][i] == max(stratagy[field]):
                choices.append(trump[i])
        guess = random.choice(choices)
    else:                                                     # if no stratagy than select randme responce
        guess = random.choice(trump)

    prev_me[0] = guess
    return guess
