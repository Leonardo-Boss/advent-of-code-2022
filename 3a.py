def valueofrucksack(l):
    r = 0
    for i in l:
        l_ascii = ord(i)
        r += l_ascii - 64 + 26 if l_ascii <= 90 else l_ascii - 96 
    return r

with open('input3.txt') as f:
    sum = 0
    letters = set()
    sumuniquer = 0
    for line in f:
        l = int(len(line)/2)
        half1 = line[:l]
        half2 = line[l:]
        # print(line)
        # print(half1)
        # print(half2)
        rucksack = set()
        for letter in half1:
            if letter in half2:
                rucksack.add(letter)
                v = valueofrucksack({letter})
                letters.add(letter)
                print(f'{letter}:{v}')
                sum += v
        sumuniquer += valueofrucksack(rucksack)
print(f'sum of all items: {sum}')
print(f'sum of all unique items: {valueofrucksack(letters)}')
print(f'sum of all unique rucksack: {sumuniquer}')
