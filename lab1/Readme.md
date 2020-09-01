# About this lab

Given a text file the program counts the occurrence of all the words in the text file and outputs the results to another text file in the same directory. It excludes white space, punctuation marks, and any other symbol. Word counter is also case insensitive so words that are capitalized are not treated as another word from its lower cased version.

# What this directory contains
* wordCount.py (python script to run)
* file1.txt (test file containing words to test the script)
* file2.txt (this is the output file, the results from running the script on a txt file are written here. If run on a different file this file gets overwritten)
* declaration.txt (used to test on script, from parent directory)

# How to use wordCount.py
command:
```
python wordCount.py <file name with txt extension>
```
run the script and provide a .txt file thats going to be used after the script name.

# How it works
The file argument is read and stored as a file object with python. Then each line of the file is traversed. While each line is being traversed the text is being stripped of extra white space at the beginning and end and symbols, then uppercase words are converted to lowercase. Each word is
is parsed into a list using .split(). From the we traverse each word in the list and compare them to a key in a dictionary. If the word doesn't exist it is placed in the dictionary as a key and given the value one, otherwise if the word matches a key the value of that key is increased by one. The dictionary is then sorted into a new dictionary using .sorted(). Then the sorted dictionary is printed into a file named "file2" this is done by traversing each key value pair in the sorted dictionary. If "file2" exists it just gets written over by the new results.
