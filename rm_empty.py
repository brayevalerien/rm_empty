import os
import sys
import tkinter as tk
import tkinter.filedialog as fd

def rm_empty(dir_path: str, rm_files: bool=False) -> list:
    """
    Recursively removes all empty directories within the given directory and
    returns the number of deleted directories.

    Args:
        dir_path (str): the path to the directory to be cleaned.
        rm_files (bool): whether to remove the empty files found or not. 

    Returns:
        list: the number of directories and the number of files that have been removed during the process.
    """
    rm_count = [0, 0]
    if not os.path.isdir(dir_path): # handles the case where directory path is wrong
        if os.path.isfile(dir_path) and rm_files:
            if os.stat(dir_path).st_size == 0:
                os.remove(dir_path)
                rm_count[1] += 1
            else:
                print(f"WARNING: {dir_path} is not empty.")
        else:
            print(f"ERROR: {dir_path} is not a directory.")
        return -1
    ls = os.listdir(dir_path)
    for item in ls:
        item_path = os.path.join(dir_path, item)
        if os.path.isdir(item_path):
            sub_rm_count = rm_empty(item_path, rm_files)
            rm_count[0] += sub_rm_count[0]
            rm_count[1] += sub_rm_count[1]
        elif os.path.isfile(item_path) and rm_files:
            if os.stat(item_path).st_size == 0:
                os.remove(item_path)
                rm_count[1] += 1
    if not os.listdir(dir_path): # case where the directory is empty
        os.rmdir(dir_path)
        rm_count[0] += 1
    return rm_count

def select_dir():
    dir = fd.askdirectory()
    dir_entry.delete(0, tk.END)
    dir_entry.insert(0, dir)

def gui_rm_empty():
    dir = dir_entry.get()
    nb_rm = rm_empty(dir)
    if nb_rm == -1: # invalid path
        nb_dirs_rm_label.config(text=f"ERROR: {dir} is not a directory.")
    else:
        nb_dirs_rm_label.config(text=f"Removed {nb_rm[0]} directorie(s) and {nb_rm[1]} file(s).")
    dir_entry.delete(0, 'end')


if __name__ == "__main__":
    rm_files = False
    if len(sys.argv) == 1: # open gui
        # main window
        window = tk.Tk()
        window.title("rm empty")

        # label displaying the selected directory
        dir_label = tk.Label(window, text="Selected directory")
        dir_label.pack()

        # entry to enter the path of the directory to cleanup
        dir_entry = tk.Entry(window, width=50)
        dir_entry.pack()

        # label showing the number of removed directories
        nb_dirs_rm_label = tk.Label(window, text="")
        nb_dirs_rm_label.pack()

        # button to open directory selection dialog
        select_button = tk.Button(window, text="Browse directories", command=select_dir)
        select_button.pack()

        # start button
        remove_button = tk.Button(window, text="Remove", command=gui_rm_empty)
        remove_button.pack()

        window.mainloop()
    else:
        args = sys.argv[1:] # get command ligne arguments
        # parse argument
        if "--rm-files" in args:
            rm_files = True
            args.remove("--rm-files")
        if len(args) == 1:
            if args[0] == "--no-gui":
                path_to_dir = input("Path to the directory you want to clean:   ")
            else: 
                path_to_dir = args[0]
            rm_count = rm_empty(path_to_dir, rm_files)
            print(f"Removed {rm_count[0]} directorie(s) and {rm_count[1]} file(s).")
        else:
            print("Invalid command format.\nUse: python ./rm_empty.py [--no-gui] [--rm-files] path_to_dir")