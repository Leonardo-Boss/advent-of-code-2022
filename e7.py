class FileSystem:
    def __init__(self, file) -> None:
        self.file = file
        self.dir:tuple = ({}, None)
        self.dir[0]['/\n'] = ({}, self.dir)
        self.root = self.dir
        self.size_index = []
        self.total_size = 70000000
        # self.file_reader = self.file_gen
        # self.pointer = 0
        # self.pointer_back = 0

    # def file_gen(self) -> Iterator[str]:
    #     for line in self.file.readlines():
    #         self.pointer_back = self.pointer
    #         self.pointer = self.file.tell()
    #         yield line

    # def file_back(self):
    #     self.file.seek(self.pointer_back)
    #     self.file_reader = self.file_gen()

    def read(self):
        for line in self.file:
            if line.startswith('$'):
                self.interpret_command(line)
                continue

            if line.startswith('dir'):
                line = line.split(' ')
                self.dir[0][line[1]] = ({}, self.dir)
                continue

            line = line.split(' ')
            self.dir[0][line[1]] = int(line[0])

    def interpret_command(self, command):
        command = command.split(' ')
        match command[1]:
            case 'cd':
                self.cd(command[2])
            case 'ls\n':
                self.ls()

    def cd(self, arg):
        if arg == '..\n':
            if self.dir[1]:
                self.dir = self.dir[1]
            return
        self.dir = self.dir[0][arg]

    def ls(self):
        # while line := self.file_reader():
        #     print(line)
        #     if line.startswith('$'):
        #         self.file_back()
        #         return

        #     line = line.split(' ')

        #     if line.startswith('dir'):
        #         self.dir[0][line[1]] = ({}, self.dir)
        #         continue

        #     self.dir[0][line[1]] = int(line[0])
        pass

    def __calc_size(self, dir):
        size = 0
        size_d = 0
        for i in dir[0].values():
            if isinstance(i, tuple):
                size_d += self.__calc_size(i)
                continue
            size += i
        size += size_d
        self.size_index.append(size)
        return size

    def create_size_index(self):
        self.__calc_size(self.root)
        self.size_index.sort()

    def free_up_space(self, target):
        if len(self.size_index) == 0: self.create_size_index()
        needed = target - (self.total_size - self.size_index[-1])
        for i in self.size_index:
            if i >= needed:
                return i

if __name__ == "__main__":
    with open('input7.txt') as f:
        fs = FileSystem(f)
        fs.read()
        fs.create_size_index()
        smallest_target = None
        total_small_folders = 0
        for i in fs.size_index:
            if i <= 100000:
                total_small_folders += i
        print(f'a: {total_small_folders}')
        print(f'b: {fs.free_up_space(30000000)}')
