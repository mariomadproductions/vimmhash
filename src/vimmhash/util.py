#util
#Version: v0.1.2
#(SemVer 2.0.0)
#UUID: 3174dba7-4b13-450d-8ab9-ce8e11408702
import sys
import contextlib
import builtins

#based on https://stackoverflow.com/questions/1744989/read-from-file-or-stdin/29824059#29824059
@contextlib.contextmanager
def open(file, mode, *args, **kwargs):
    if file == '-':
        if mode is None or mode == '' or 'r' in mode:
            fh = sys.stdin
        else:
            fh = sys.stdout
    else:
        fh = builtins.open(file, mode)
    try:
        yield fh
    finally:
        if file != '-':
            fh.close()
