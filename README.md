# rm_empty - A Handy Tool to Remove Useless Empty Files and Directories

## Overview
`rm_empty` is a utility tool designed to clean up unnecessary empty directories and empty files from any location on your system. I initially made it to clean-up files stored on SD cards that went into phones, drones or camera, which usually create a bunch of useless system files and directories.

## How to Use
There are two simple ways to use `rm_empty`: with a Graphical User Interface (GUI) or through the command line.

### Using the GUI
To access the GUI, follow these easy steps:
1. Open a terminal.
2. Run the command `python rm_empty.py`.
3. A small window will appear (see following screenshot), offering you two options:
   - **Enter Path Manually**: You can type in the path of the directory you want to clean up.
   - **Browse Directories**: Click on the "Browse directories" button to conveniently select the target directory.

![UI window](./ui.png)

**Note:** Make sure you have the `tkinter` library properly installed to utilize the GUI.

### Using the Terminal
For command-line enthusiasts, `rm_empty` offers a straightforward method:
1. Open a terminal.
2. Run the command bellow to clean the specified directory at `dir_to_path`. If you include the `--rm-files` flag, the utility will remove empty files as well.
```bash
python rm_empty.py [--rm-files] dir_to_path
```
3. Alternatively, run `python rm_empty --no-gui`, and the program will prompt you to enter the path of the directory you wish to clean.

## Upcoming Features
We are continuously working to enhance this small but powerful script. The following features are currently in development:
- [x] Option to remove empty files.
- [ ] GUI support for empty file removal: at the moment, using the GUI will, by default, not remove empty files.

Feel free to contribute to the project, report issues, create pull requests, or suggest new ideas.