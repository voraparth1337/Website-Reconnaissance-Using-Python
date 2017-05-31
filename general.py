# written by Parth V
# general operations


import os


def create_dir(directory):
    '''
    Function creates a directory if it doesnt exist - for each url one directory
    :param directory: path 
    :return: void
    '''
    if not os.path.exists(directory):
        os.makedir(directory)


def write_file(path, data):
    '''
    Function writes data to the file whose path is specified
    :param path: Path to the file
    :param data: Data to be written to the file
    :return: void
    '''
    with open(path, 'w') as f:
        f.write(data)
        f.close()
