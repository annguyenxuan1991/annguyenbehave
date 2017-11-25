import os


def get_file_by_relative_path(path_fragment):
    directory = os.path.dirname(__file__)
    return os.path.join(directory, path_fragment)
