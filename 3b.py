def valueofrucksack(l):
    r = 0
    for i in l:
        l_ascii = ord(i)
        r += l_ascii - 64 + 26 if l_ascii <= 90 else l_ascii - 96 
    return r

def find_badge(f):
    line1 = f.readline()
    line2 = f.readline()
    line3 = f.readline()
    for l in line1:
        if l in line2 and l in line3:
            return l

with open('input3.txt') as f:
    badges = []
    badge = find_badge(f)
    while badge:
        badges.append(badge)
        badge = find_badge(f)

print(valueofrucksack(badges))
