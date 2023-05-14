def jankenpon(player1, outcome):
    score = 0
    result  = {'X': 0, 'Y': 3, 'Z': 6}
    winning = {'A': 'B', 'B': 'C', 'C': 'A'}
    losing  = {'A': 'C', 'B': 'A', 'C': 'B'}
    hand    = {'A': 1, 'B': 2, 'C': 3}
    score += result[outcome]
    if score == 0:
        score += hand[losing[player1]]
    elif score == 3:
        score += hand[player1]
    elif score == 6:
        score += hand[winning[player1]]
    return score

with open('input2.txt', 'r') as f:
    score = 0
    for line in f:
        score += jankenpon(line[0], line[2]) 

print(score)
