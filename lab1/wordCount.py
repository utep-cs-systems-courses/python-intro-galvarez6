import os
import re
import sys

#open the file using the open() to return a file object
#file is in the same directory as the py file
#file1 = open("file1", "r")

# now we want to take the file as a parameter from the command line
# instead of being hard coded so
# we import sys and use
file1 = open(sys.argv[1], "r")

#test to see if the file opens with read()
#the "name" attribute of the the file object gives us the path of the fileobject
#'\033[1m' + string + '\033[0m' makes the text bold on the terminal
#print('\033[1m' + '\nfrom file: '+ file1.name + '\033[0m')
#print(file1.read()+'\n')

#create a dictionary to place the text into
#a dictionary in python is an associative array
#it can store key value pairs
#so it can store the word and the number of times it occures
wordCounter = dict()
wordList = []

#go through each line of the fileobject
for text in file1:
    #just in case we want to remove leading and
    #ending white spaces (given a parameter it can also remove
    #leading un-wanted characters like if we wanted to remove
    # leading and ending ,, or letteres it would be text.strip(",abc"))
    text = text.strip()

    #we also want all capital letter to be replaced with
    # lower case so instances like A and a dont count twice
    #lower returns the lowercases string from the uppercase
    text = text.lower()

    #then we can strip the text of any puncuation marks
    #this is using regular expressions
    text = res = re.sub(r'[^\w\s]', '', text)
    #otherwise i can define all the marks to be omitted like this
    #punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
    #for ele in test_str:
    #if word in text:
        #test = test.replace(ele, "")

    #then we want to seperate each word
    #using split with " " we can seperate the text
    #block into a string
    wordList = text.split()

    ############ word list test ##############
    #test our word list to see if it split properly
    #(it does work so im gonna comment this out)

    #print(wordList)
    ##########################################

    ### check if words in the list are in the dictionary ########
    #now we iterate through our word list
    #check if the current word is in the dictionary already
    #if it is increment the dictionary word key value by 1
    #if not
    #add the current word to the dictionary
    #also add 1 to to it in the dictionary
    for word in wordList:
        if word in wordCounter:
            #the word is the key and the value is the amount of
            #instances of the key in the dictionary
            wordCounter[word] +=1
        else:
            #else if it doesnt exist add word (key) to dictionary
            #and assign its value to 1 like this
            ## Dictionary_Name[New_Key_Name] = New_Key_Value
            wordCounter[word] = 1
    ###############################################


########## then we can sort the directory #########
## we can use sorted to sort the keys
# but we also have to typecast it to dictionary
# because sorted returns a list of items
#key is used to transform items before they are compared
# lambda is an anonymous function used with sorted
sortedWordCoutner = dict( sorted(wordCounter.items(), key=lambda x: x[0].lower()) )

#test before and after it works
#print(wordCounter)
#print(sortedWordCoutner)

##################################################


#### print the dictionary to a new file#######

file2 = open("file2.txt", "w")
for key in sortedWordCoutner:
    file2.write(key + " : " + str(sortedWordCoutner[key]) +"\n")

file2 = open("file2.txt", "r")
print("\n")
print(file2.read())



########### create and read other file############
#i also want to test outputing to another file
#so im just gonna print whats in file1 to a file2 to see
#if i can achieve output to another file
#use open again but replace r with "a" or "w" or "x"
#a appends to end of a file and w overwrites everything in an existing file1
#x create a file and will return an error if file exists

#file2 = open("file2.txt", "w")

#then use attribute write()

#file2.write("file")
#file2 = open("file2.txt", "r")
#print('\033[1m' + '\nfrom file: '+ file2.name + '\033[0m')
#print(file2.read() + "\n")
################################################


#close() funciton closes file and frees memory
#close file when down with them

file2.close()
