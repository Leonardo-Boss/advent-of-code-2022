with open('input.txt', 'r') as f:
    elve = 0
    n = 3
    top = [0 for _ in range(n)]
    for line in f:
        if line == '\n':
            for i in range(n):
                if top[i] <= elve:
                    top.insert(i, elve)
                    print(f'inserted {elve}, removed {top.pop(n)}')
                    print(top)
                    break
            elve = 0
        else:
            elve += int(line)
print(sum(top))
