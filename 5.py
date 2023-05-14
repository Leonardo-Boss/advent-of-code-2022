from collections import deque
# from itertools import islice
import regex as re

class Crane9000:
    def __init__(self) -> None:
        self.base = {i:deque() for i in range(9)}

    def get_top(self):
        return ''.join((i[-1] for i in self.base.values()))

    def read_header(self, f):
        for line in f:
            if line == '\n':
                break
            pointer = 0
            for i in range(9):
                pointer += 1
                if line[pointer].isalpha():
                    self.base[i].appendleft(line[pointer])
                pointer += 3

    def move(self, n, f, t):
        for _ in range(n):
            container = self.base[f].pop()
            self.base[t].append(container)

    def read_instructions(self, file):
        for line in file:
            n, f, t = re.findall(r'[0-9]+', line)
            n, f, t = int(n), int(f) - 1, int(t) - 1
            self.move(n, f, t)

class Crane9001(Crane9000):
    def __init__(self) -> None:
        self.base = {i:list() for i in range(9)}

    def read_header(self, f):
        for line in f:
            if line == '\n':
                break
            pointer = 0
            for i in range(9):
                pointer += 1
                if line[pointer].isalpha():
                    self.base[i].insert(0, line[pointer])
                pointer += 3

    def move(self, n, f, t):
        cargo = self.base[f][-n:]
        self.base[f] = self.base[f][:-n]
        self.base[t].extend(cargo)
        # l = len(self.base[f])
        # x = l-n-1 if l-n-1 >= 0 else 0
        # cargo = deque(islice(self.base[f], x))
        # self.base[f] = deque(islice(self.base[f], 0, x))
        # self.base[t].extend(cargo)

if __name__ == "__main__":
    cr0 = Crane9000()
    cr1 = Crane9001()
    with open('input5.txt') as f:
        cr0.read_header(f)
        cr0.read_instructions(f)
        print('crane9000:', cr0.get_top())

        f.seek(0)

        cr1.read_header(f)
        cr1.read_instructions(f)
        print('crane9001:', cr1.get_top())
