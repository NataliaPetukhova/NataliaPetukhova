import os


class FileSystemError(Exception):
    ''' Class for errors in filesystem module '''
    pass
        


class FSItem(object):
    ''' Common class for OS items OS: Files and Directories '''

    def __init__(self, path):
        ''' Creates new FSItem instance by given path to file '''
        self.path = path


    def rename(self, newname):
        ''' Renames current item
                raise FileSystemError if item does not exist
                raise FileSystemError if item "newname" already exists '''
        if self.getname() == newname:
            raise FileSystemError("Item {0} already exists".format(newname))
        elif not os.path.exists(self.path):
            raise FileSystemError("File {0} does not exist".format(self.getname()))
        else:
            return os.rename(self.path, os.path.join(os.path.dirname(self.path),newname))


    def create(self):
        ''' Creates new item in OS
                raise FileSystemError if item with such path already exists '''
        if os.path.exists(self.path):
            raise FileSystemError("Item {0} with such path already exists".format(self.getname()))
        else:
            return os.makedirs(os.path.dirname(self.path))


    def getname(self):
        ''' Returns name of current item '''
        return os.path.basename(self.path)


    def isfile(self):
        ''' Returns True if current item exists and current item is file, False otherwise '''
        if os.path.isfile(self.path):
            return True
        else:
            return False


    def isdirectory(self):
        ''' Returns True if current item exists and current item is directory, False otherwise '''
        if os.path.isdir(self.path):
            return True
        else:
            return False



class File(FSItem):
    ''' Class for working with files '''

    def __init__(self, path):
        ''' Creates new File instance by given path to file
                raise FileSystemError if there exists directory with the same path '''
        self.path = path
        if os.path.isdir(self.path):
            raise FyleSystemError("Item {0} is a directory".format(self.getname()))


    def __len__(self):
        ''' Returns size of file in bytes
                raise FileSystemError if file does not exist '''
        if not os.path.exists(self.path):
            raise FileSystemError("File {0} does not exist".format(self.getname()))
        else:
            os.path.getsize(self.path)
            

    def getcontent(self):
        ''' Returns list of lines in file (without trailing end-of-line)
                raise FileSystemError if file does not exist '''
        if not os.path.exists(self.path):
            raise FileSystemError("File {0}does not exist".format(self.getname()))
        else:
            return len(self.text(encoding, errors).splitlines(retain))


    def __iter__(self):
        ''' Returns iterator for lines of this file
                raise FileSystemError if file does not exist '''
        if not os.path.exists(self.path):
            raise FileSystemError("File {0} does not exist".format(self.getname()))
        else:
            return iter(self.getcontent())



class Directory(FSItem):
    ''' Class for working with directories '''

    def __init__(self, path):
        ''' Creates new Directory instance by given path
                raise FileSystemError if there exists file with the same path '''
        self.path = path
        if os.path.isfile(self.path):
            raise FyleSystemError("Item {0} is a file".format(self.getname()))


    def items(self):
        ''' Yields FSItem instances of items inside of current directory
                raise FileSystemError if current directory does not exists '''
        if not self.path.exists(self.path):
            raise FileSystemError("File {0} does not exist".format(self.getname()))
        return os.listdir(self.path)


    def files(self):
        ''' Yields File instances of files inside of current directory
                raise FileSystemError if current directory does not exists '''
        if not self.path.exists(self.path):
            raise FileSystemError("File {0} does not exist".format(self.getname()))
        else:
            return [f for f in self.items() if File(os.path.join(self.path, f)).isfile()]


    def subdirectories(self):
        ''' Yields Directory instances of directories inside of current directory
                raise FileSystemError if current directory does not exists '''
        if not self.path.exists(self.path):
            raise FileSystemError("File {0} does not exist".format(self.getname()))
        else:
            return next(os.walk(self.path))


    def filesrecursive(self):
        ''' Yields File instances of files inside of this directory,
                inside of subdirectories of this directory and so on...
                raise FileSystemError if directory does not exist '''
        if not self.path.exists(path):
            raise FileSystemError("File {0} does not exist".format(self.getname()))
        else:
            return [x for x in os.walk(self.path)]


    def getsubdirectory(self, name):
        ''' Returns Directory instance with subdirectory of current directory with name "name"
                raise FileSystemError if item "name" already exists and item "name" is not directory '''
        if self.getname() == newname:
            raise FileSystemError("Item {0} already exists".format(newname))
        elif not self.path.isdir(self.path):
            raise FileSystemError("Item {0} is not a directory".format(self.getname()))
        else:
            for x in os.listdir(self.path):
                if os.path.isfile(x.path):
                    return file(x.path)
                else:
                    return dir(x.path)


if __name__ == '__main__':
    path1 = File("C:/Users/Natalia/Desktop/test.txt")
    print(path1.__len__())
    print(path1.rename("py.txt"))

    path2 = Directory("C:/Users/Natalia/Desktop/New")
    path2.rename("Folder")
    print(path2.getname())
    print(path2.subdirectories())
    print(path2.filesrecursive())
    print(path2.getsubdirectory("directory"))
    
    

        

