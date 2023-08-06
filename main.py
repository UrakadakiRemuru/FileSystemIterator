from os import walk
class FileSystemIterator:
    def __init__(self, root: str, only_files: bool, only_dirs: bool, pattern: str):
        self.root = root
        self.only_files = only_files
        self.only_dirs = only_dirs
        self.pattern = pattern
    def __iter__(self):
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
                            yield root_txt + '/' + k
                        elif self.pattern is None:
                            yield root_txt + '/' + k
for i in FileSystemIterator('E:\pycharmprojects', False, False, None):
    print(i)