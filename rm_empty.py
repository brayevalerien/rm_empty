import os
import sys
import tkinter as tk
import tkinter.filedialog as fd

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
        return -1
    ls = os.listdir(dir_path)
    for item in ls:
        item_path = os.path.join(dir_path, item)
        if os.path.isdir(item_path):
            rm_count += rm_empty(item_path)
    if not os.listdir(dir_path): # case where the directory is empty
        os.rmdir(dir_path)
        rm_count += 1

    return rm_count

def select_dir():
    dir = fd.askdirectory()
    dir_entry.delete(0, tk.END)
    dir_entry.insert(0, dir)

def gui_rm_empty():
    dir = dir_entry.get()
    nb_dirs_rm = rm_empty(dir)
    if nb_dirs_rm == -1: # invalid path
        nb_dirs_rm_label.config(text=f"ERROR: {dir} is not a directory.")
    else:
        nb_dirs_rm_label.config(text=f"Removed {nb_dirs_rm} empty directories.")
    dir_entry.delete(0, 'end')


if __name__ == "__main__":
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
        select_bouton = tk.Button(window, text="Browse directories", command=select_dir)
        select_bouton.pack()

        # start button
        nettoyer_bouton = tk.Button(window, text="Remove", command=gui_rm_empty)
        nettoyer_bouton.pack()

        window.mainloop()
    else:
        args = sys.argv[1:] # get command ligne arguments
        # parse argument
        if len(args) == 1:
            if args[0] == "--no-gui":
                path_to_dir = input("Path to the directory you want to clean:   ")
            else: 
                path_to_dir = args[0]
            rm_count = rm_empty(path_to_dir)
            print(f"Removed {rm_count} empty directories.")
        else:
            print("Invalid command format.\nUse: python ./rm_empty.py [--no-gui] path_to_dir")