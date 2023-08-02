from os import walk
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
                        yield root_txt + '/' + k
                    elif pattern is None:
                        yield root_txt + '/' + k

for i in degenerator('C:/users/mdemin/testdir', only_files=True, pattern='dd'):
    print(i)
d = degenerator('C:/users/mdemin/testdir')
next(d)
next(d)