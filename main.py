from os import walk
from pathlib import Path
class FileSystemIterator:
    def __init__(self, root: str, only_files: bool, only_dirs: bool, pattern):
        self.root = root
        self.only_files = only_files
        self.only_dirs = only_dirs
        self.pattern = pattern

    def degenerator(self, root: str, only_files: bool, only_dirs: bool, pattern):
        root_txt = ''
        for i in walk(root):
            for j, val in enumerate(i):
                if j == 0:
                    root_txt = val
                else:
                    if only_files and j == 1:
                        continue
                    if only_dirs and j == 2:
                        break
                    for k in val:
                        if pattern is not None and pattern in k:
                            yield Path(root_txt + '/' + k)
                        elif pattern is None:
                            yield Path(root_txt + '/' + k)
    def __iter__(self):
        return self.degenerator(self.root, self.only_files, self.only_dirs, self.pattern)
    def __next__(self):
        if not self.__iter__:
            raise StopIteration
        else:
            return next(self.degenerator(self.root, self.only_files, self.only_dirs, self.pattern))


d = FileSystemIterator('E:\pycharmprojects/nic/testdir', False, False, None)
for i in d:
    print(i)
print(next(d))
print(next(d))
print(next(d))










