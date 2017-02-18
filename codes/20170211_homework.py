#!/usr/bin/env python
import pwd
import grp
import stat

import pathlib
import argparse
import datetime 
parser = argparse.ArgumentParser(prog="ls",add_help=False)
parser.add_argument('-l',dest="long_format",help="",action="store_true")
parser.add_argument('-h',dest="human",help='',action="store_true")
parser.add_argument('-a',dest='all',help='',action="store_true")
parser.add_argument('path',nargs='*',default='.')

args = parser.parse_args()

def scan(path:str):
    yield from {x for x in pathlib.Path(path).iterdir() if args.all }

def time_format(mtime: int) -> str:
    dt = datetime.datetime.fromtimestamp(mtime)
    return '{:>2} {:>2} {:>2}:{:>2}'.format(dt.month,dt.day,dt.hour,dt.minute)

def size_setup(size: int) -> str:
    if not args.human:
        return str(size)
    units = ['','K','M','G','T','P',]

def format(item: pathlib.Path) -> str:
    if not args.long_format:
        return item.name

    st = item.stat()
    attr = {
        'mode':stat.filemode(st.st_mode),
        'nlink': st.st_nlink,
        'user': pwd.getpwuid(st.st_uid).pw_name,
        'group': grp.getgrgid(st.st_gid).gr_name,
        'size': st.st_size,
        'mtime':time_format(st.st_mtime),
        'name': item.name
    }
    return '{mode} {nlink} {user} {group} {size} {mtime} {name}'.format(**attr)