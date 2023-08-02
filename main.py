from os import walk
class FileSystemIterator:
    def __init__(self, root: str, only_files: bool, only_dirs: bool, pattern: str):
        self.root = root
        self.only_files = only_files
        self.only_dirs = only_dirs
        self.pattern = pattern
        self.degenerator(self.root, self.only_files, self.only_dirs, None)
    def degenerator(self, root: str, only_files: bool, only_dirs: bool, pattern) -> str:
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
                            yield root_txt + '/' + k
                        elif pattern is None:
                            yield root_txt + '/' + k
for i in FileSystemIterator('C:/users/mdemin/testdir', False, False, None):
    print(i)