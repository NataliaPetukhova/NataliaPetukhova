import os
import sys
import shutil

from Task9 import *


def main(args):
    cwd = Directory(os.getcwd())
    while True:
        cmdtokens = input('{path}$ '.format(path=cwd.path)).split()
        if not cmdtokens:
            continue
        cmd = cmdtokens[0]
        cmdargs = cmdtokens[1:]

        if cmd == 'ls':
            print()
            path = cwd.path if not cmdargs else cmdargs[0]
            directory = cwd.getsubdirectory(path)
            for item in directory.items():
                if item.isfile():
                    print('{name}\tFILE\t{size}'.format(name=item.getname(), size=len(item)))
                else:
                    print('{name}\tDIR'.format(name=item.getname()))
            print()
        elif cmd == 'cd':
            newpath = ''.join(cmdargs)
            if os.path.exists and os.path.isdir(newpath):
                os.chdir(newpath)
                cwd = Directory(os.getcwd())
                print(cwd.path)
            else:
                print("There is no such directory")
                raise FileSystemError
        elif cmd == 'cat':
            newpath = ''.join(cmdargs)
            if os.path.isfile(newpath):
                print(newpath.getcontent())
            else:
                raise FileSystemError("There is no file {0}".format(newpath))
        elif cmd == 'head':
            newpath = ''.join(cmdargs)
            if os.path.isfile(newpath):
                with open(newpath, 'r') as file:
                    alllines = file.readlines()
                    for head in alllines[10:]:
                        print(head)
        elif cmd == 'tail':
            newpath = ''.join(cmdargs)
            if os.path.isfile(newpath):
                with open(newpath, 'r') as file:
                    alllines = file.readlines()
                    for tail in alllines[-10:]:
                        print(tail)
        elif cmd == 'pwd':
            newpath = ''.join(cmdargs)
            print(newpath)
        elif cmd == 'touch':
            newpath = ''.join(cmdargs)
            File(newpath).filecreate()
        elif cmd == 'find':
            pass
        elif cmd == 'mv':
            oldname = cmdargs[0]
            newname = cmdargs[1]
            if os.path.exists(oldname) and not os.path.exists(os.path.join(os.getcwd(), newname)):
                os.rename(oldname, newname)
        elif cmd == 'cp':
            oldname = cmdargs[0]
            newname = cmdargs[1]
            shutil.copy(oldname, newname)
        elif cmd == 'clear':
            os.system('cls')
        elif cmd == 'exit':
            print("Bye bye!")
            break
        else:
            print('Unknown command: {cmd}'.format(cmd=cmd))


if __name__ == '__main__':
    main(sys.argv)
