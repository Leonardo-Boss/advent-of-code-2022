def jankenpon(player1, player2):
    score = 0
    if (player1, player2) in (('A', 'Y'), ('B', 'Z'), ('C', 'X')):
        print('player1')
        score +=  6
    elif (player1, player2) in (('A', 'Z'), ('B', 'X'), ('C', 'Y')):
        print('player2')
        score += 0
    else:
        print('tie')
        score += 3
    score += {'X':1, 'Y':2, 'Z':3}[player2]
    return score

with open('input2.txt', 'r') as f:
    score = 0
    for line in f:
        score += jankenpon(line[0], line[2]) 

print(score)
