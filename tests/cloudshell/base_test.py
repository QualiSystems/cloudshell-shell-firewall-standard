import os


def find_package_dir(cur_dir=None):
    if cur_dir is None:
        cur_dir = os.path.dirname(__file__)

    if "setup.py" in os.listdir(cur_dir):
        return cur_dir

    parent_dir = os.path.dirname(cur_dir)
    return find_package_dir(parent_dir)


PACKAGE_DIR = find_package_dir()
