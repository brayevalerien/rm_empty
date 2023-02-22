import os


def rm_empty(dir_path: str) -> int:
    """
    Recursively removes all empty directories within the given directory and
    returns the number of deleted directories.

    Args:
        dir_path (str): the path to the directory to be cleaned.

    Returns:
        int: the number of directories that have been removed during the process.
    """
    rm_count = 0
    if not os.path.isdir(dir_path): # handles the case where directory path is wrong 
        print(f"ERROR: {dir_path} is not a directory.")
        return rm_count
    ls = os.listdir(dir_path)
    for item in ls:
        item_path = os.path.join(dir_path, item)
        if os.path.isdir(item_path):
            rm_count += rm_empty(item_path)
    if not os.listdir(dir_path): # case where the directory is empty
        os.rmdir(dir_path)
        rm_count += 1

    return rm_count

if __name__ == "__main__":
    dir_path = "./test - Copie" # change this to the directory you want to clean. TODO: replace this by the call arguments using sys.
    rm_count = rm_empty(dir_path)
    print(f"Removed {rm_count} directories in {dir_path} .")