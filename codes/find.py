import argparse
import pathlib
import datetime
import grp
import stat
import fnmatch


parser = argparse.ArgumentParser(prog='find')
parser.add_argument('path')
parser.add_argument('-name',dest='name',type=str,default='*')
parser.add_argument('-executable',dest='executable',action='store_true')


args = parser.parse_args()

def _walk(path: pathlib.Path,):
    for item in path.iterdir():
        if item.is_dir():
            yield from _walk(item)
        yield item

def walk(path):
    yield from _walk(pathlib.Path(path))

def is_name_match(item:pathlib.Path,pattern:str) ->bool:
    return fnmatch.fnmatch(str(item),pattern)

def is_executable(item:pathlib.Path) -> bool:
    mode = item.lstat().st_mode
    return stat.S_IEXEC & mode > 0

def filter(item:pathlib.Path) -> bool:
    ret = is_name_match(item,args.name)
    if args.executable:
        ret = ret and is_executable(item)

    return ret


def main():
    for item in walk(args.path):
        if filter(item):
            print(item)

if __name__ == "__main__":
    main()