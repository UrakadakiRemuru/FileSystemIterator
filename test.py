from os import walk
from pathlib import Path
class FileSystemIterator:
    def __init__(self, root, only_files, only_dirs, pattern):
        self.root = root
        self.only_files = only_files
        self.only_dirs = only_dirs
    def __iter__(self):
        return self
    def next(self):
        if not self.__iter__():
            raise StopIteration
        current_dir = os.path.join(self.root, self.current_path)
        if self.is_directory_only:
            yield current_dir
        else:
            for file in os.listdir(current_dir):
                yield file
def degenerator(root: str, only_files=False, only_dirs=False, pattern=None) -> str:
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

for i in degenerator('C:/users/mdemin/testdir'):
    print(i)
d = degenerator('C:/users/mdemin/testdir')
marker = True
try:
    while marker:
        print(next(d))
except StopIteration:
    marker = False
    print('Пизда')