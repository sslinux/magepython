#!/usr/bin/env python

import argparse
import pathlib
import stat
import pwd
import grp
import datetime

parser = argparse.ArgumentParser(prog='ls',add_help=True)

parser.add_argument('-l',dest="long_format",help='long format',action='store_true')
parser.add_argument('-h',dest='human',help='human readable',action='store_true')
parser.add_argument('-a',dest='all',help='all include . and ..',action='store_true')
parser.add_argument('path',nargs='*',help='which path you want to list.',default='.')

args = parser.parse_args()


def scan(path:str):
    yield from (x for x in pathlib.Path(path).iterdir() if args.all or not x.name.startswith('.'))

def time_format(mtime:int) -> str:
    dt = datetime.datetime.fromtimestamp(mtime)
    return '{:>2} {:>2} {:>2} {:>2}'.format(dt.month,dt.day,dt.hour,dt.minute)

def size_setup(size:int) -> str:
    if not args.human:
        return str(size)

    units = ['','K','M','G','T','P','E']
    idx = 0
    while size > 1024:
        size /= 1024
        idx += 1
    return '{} {}'.format(round(size,1),units[idx])

def format(item:pathlib.Path) -> str:
    if not args.long_format:
        return item.name
    st = item.stat()
    attr = {
        'mode': stat.filemode(st.st_mode),
        'nlink': st.st_nlink,
        'user': pwd.getpwuid(st.st_uid).pw_name,
        'group': grp.getgrgid(st.st_gid).gr_name,
        'size': size_setup(st.st_size),
        'mtime':time_format(st.st_mtime),
        'name':item.name
    }
    return '{mode} {nlink} {user} {group} {size} {mtime} {name}]'.format(**attr)

def main():
    if isinstance(args.path,list):
        for path in args.path:
            print('{}'.format(path))
            for item in scan (path):
                print(format(item))
            print()
    else:
        for item in scan(args.path):
            print(format(item))


if __name__ == "__main__":
    main()