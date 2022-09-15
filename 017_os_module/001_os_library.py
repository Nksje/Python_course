import os
import time

### Getting stared
# List all methods of OS module
print(dir(os))

# Get current working directory
print(os.getcwd())

# Change current working directory
os.chdir('C:\\Users\\Kasutaja\\PycharmProjects\\course_python_nov')
print(os.getcwd())

# Get a list of files and folders in directory
print(os.listdir())


### Creating new directories inside current directory
# mkdir creates one folder
# os.mkdir('new_folder')

# makedirs creates many folders inside one another
os.makedirs('new_folder2/sub_folder/sub_folder1')


time.sleep(3)
# rmdir removes last directory (exact directory) in ()
os.rmdir('new_folder2/sub_folder/sub_folder1')

# removedirs removes all directories in ()
os.removedirs('new_folder2/sub_folder/sub_folder1')


### Renaming a directory or file
os.rename('sample.txt', 'sample.txt')


### Print information about file or directory
print(os.stat('sample.txt'))

# Each stat can be called separately
print(os.stat('sample.txt').st_size)  # Size in bytes
print(os.stat('sample.txt').st_mtime)  # Last modification time (timestamp)


### Getting information on many directories
information = os.walk('C:\\Users\\Kasutaja\\PycharmProjects\\course_python_nov')
print(information)

# os.walk() creates an iterable object, dirpath, dirnames, filenames are information types it uses.
for dirpath, dirnames, filenames in information:
    print('Current path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    print('\n')


## Calling environment variables and working with path
print(os.environ)
print(os.environ.get('HOMEPATH'))

# Direct method. Easy to miss /
file_path = os.environ.get('HOMEPATH') + '\\sample.txt'
print(file_path)

# os.path method automatically joins path
file_path = os.path.join(os.environ.get('HOMEPATH'), 'sample.txt')
print(file_path)

# os.path.basename() will grab filename from path string. Doesn't have to exist.
print(os.path.basename('/somedir/dir2/sample.txt'))

# os.path.dirname() will grab directory from path string. Doesn't have to exist.
print(os.path.dirname('/somedir/dir/2text.txt'))

# os.path.split() will grab both and return a tupple
print(os.path.split('/somedir/dir2/sample.txt'))

# os.path.exists() returns boolean. True if exists False if not.
print(os.path.exists('/somedir/dir2/sample.txt'))

# check if is file or is directory. Returns boolean
print(os.path.isdir('sample.txt'))
print(os.path.isfile('sample.txt'))

# Separates file extension from path string
print(os.path.splitext('/somedir/sample.txt'))

# List all methods of os.path module
print(dir(os.path))