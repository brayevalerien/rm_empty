# rm_empty
 A small utlity tool to remove all useless empty directories at a given location.

 ## How to use
 For the moment, the path of the directory you want to clean needs to be written in the source code:
 ```python
 if __name__ == "__main__":
    dir_path = "./test - Copie" # CHANGE THIS TO YOUR OWN PATH
    ...
 ```
Then you can simply run the python file from anywhere runing the following command in a terminal:
```shell
python3 ./rm_empty.py
```

## To do
The following things might be added in the future to improve this small script:
- [ ] Check for invalid arguments
- [ ] Use `sys` library to be able to run `python3 ./rm_empty.py path_to_dir` instead of changing the source code
- [ ] Add a simple UI to select the directory and run the script