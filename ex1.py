import os
import shutil

# create a directory
# loop through the letters of the alphabet -- ord()
# find all the files in a directory -- ls 
# change directories - cd
# move files to a new directory
# use string formatting to create directory names - "./%s/" % letter
# loop through file names -- see if they start with desired letter

# pseudocode:
# for each letter in the alphabet:
# create a directory with that letter as the name in the current directory

def create_directories():
    for i in range(97, 123):
        letter = chr(i)
        dir_string = "./%s/" % letter
        if os.path.exists(dir_string) == False:
            os.mkdir(dir_string)

# os.listdir() takes a string-formatted path as an argument

# Get all the files from original_files/

def get_files():
    return os.listdir('./original_files/')

# for each filename, get the letter that it starts with and put into the proper directory

def sort_files():
    files = get_files()

    for filename in files:
        file_string = './original_files/%s' % filename
        letter = filename[0]
        dir_string = "./%s/" % letter
        shutil.move(file_string, dir_string)

create_directories()
sort_files()
