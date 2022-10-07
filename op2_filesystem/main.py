import os, sys, shutil
from os.path import join, exists, isdir, isfile

file_buffer = (16*1024*1024)

if __name__ == '__main__':
    current_working_dir = os.getcwd()

    print(f': Current working directory: {current_working_dir}')
    

    print('\n\n: Writing to file :')
    while 1:
        fname = input('\nEnter file name> ')

        if exists(fname):
            print('File already exists!')
            continue

        print('Enter file data here, type "~~~" if you want to quit.')
        buffer = []
        while 1:
            buff = input('')

            if buff == '~~~': # break it!
                break

            buffer.append(buff)

        with open(fname, 'w+', buffering=file_buffer) as fd:
            fd.write("\n".join(buffer))

        break # continue to the next step

    print('\n\n: Making directory :')
    while 1:
        dirname = input('\nEnter directory name> ')
        if exists(dirname):
            print('Directory already exists!')
            continue

        os.mkdir(dirname)
        break

    print('\n\n: Removing file :')
    while 1:
        fname = input('\nEnter filename> ')
        if not exists(fname):
            print('File does not exist!')
            continue

        os.remove(fname)
        break

    print('\n\n: Removing directory :')
    while 1:
        dirname = input('\nEnter directory name> ')
        if not exists(dirname):
            print('Directory does not exist!')
            continue

        shutil.rmtree(dirname, True)
        break

    print('\n\n: Reading from file :')
    while 1:
        fname = input('\nEnter filename> ')
        if not exists(fname):
            print('File not found!')
            continue

        with open(fname, buffering=file_buffer) as fd:
            print(fd.read())

        break

    print('\n\n: Making directories with nested loop :')
    for x in range(2):
        for y in range(5):
            os.mkdir(f'dir{x+1}{y+1}')
    
    print('\n\n\n: Goodbye! :\n\n\n')
    sys.exit(0)