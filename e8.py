from collections import deque

class HeightMap:
    def __init__(self, file) -> None:
        self.file = file

    def read(self):
        l1 = self.file.readline()
        self.chunk = deque((None, None, l1), maxlen=3)
        for line in self.file:
            self.chunk.append(line)
            self.countvisible()

    def countvisible(self):
        pass
