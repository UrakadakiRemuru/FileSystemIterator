from os import walk, path
from pathlib import Path
class FileSystemIterator:
    def __init__(self, root: str, only_files: bool, only_dirs: bool, pattern):
        self.root = root
        self.only_files = only_files
        self.only_dirs = only_dirs
        self.pattern = pattern
        self.generator = self.degenerator()
        if self.only_dirs and self.only_files:
            raise ValueError
        if not path.exists(self.root):
            raise FileNotFoundError
    def degenerator(self):
        root_txt = ''
        for i in walk(self.root):
            for j, val in enumerate(i):
                if j == 0:
                    root_txt = val
                else:
                    if self.only_files and j == 1:
                        continue
                    if self.only_dirs and j == 2:
                        break
                    for k in val:
                        if self.pattern is not None and self.pattern in k:
                            yield Path(root_txt + '/' + k)
                        elif self.pattern is None:
                            yield Path(root_txt + '/' + k)
    def __iter__(self):
        return self
    def __next__(self):
        return next(self.generator)