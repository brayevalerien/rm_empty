import os

def aux_rm_empty(dir_path: str, rm_count: int) -> int:
    """Recursivly removes all empty directories contained in the directory at dir_path.
    This is an auxiliary function of rm_empty that allows the program to count how many repertories where removed.
    
    TODO:
        Handle invalid args
        Fix rm_count (it currently returns nonsense)

    Args:
        dir_path (str): path of the directory that needs to be cleaned up
        rm_count (int): count of already removed directories

    Returns:
        int: total count of removed directories
    """
    for index, (root, dirs, files) in enumerate(os.walk(dir_path)):
        if not (dirs or files): # root is a fully empty directory
            rm_count += 1
            os.rmdir(root)
        elif not dirs and files: # root only contains files
            pass
        else: # root contains at least one directoy
            for directory in dirs:
                rm_count += aux_rm_empty(root + directory + "/", rm_count)
    return rm_count

def rm_empty(dir_path: str) -> int:
    """Recursivly removes all empty directories contained in the directory at dir_path.

    Args:
        dir_path (str): path of the directory that needs to be cleaned up

    Returns:
        int: total count of removed directories
    """
    return aux_rm_empty(dir_path, 0)

if __name__ == "__main__":
    dir_path = "./test - Copie/"
    test_rm_count = rm_empty(dir_path)
    print(f"Removed {test_rm_count} empty directories")
    