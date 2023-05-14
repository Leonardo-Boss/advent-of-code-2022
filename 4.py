def makeset(string):
    b, e = string.split('-')
    b, e = int(b), int(e)
    return {i for i in range(b,e+1)}

with open('input4.txt') as f:
    contain, overlap = 0, 0
    for line in f:
        a,b = line.split(',')
        a = makeset(a)
        b = makeset(b)
        if a.issubset(b) or b.issubset(a):
            contain += 1
        if a.intersection(b):
            overlap += 1
print(f'contain: {contain}')
print(f'overlap: {overlap}')
