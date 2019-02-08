#Function to create the dictionary of anagrams from txt file
def make_anagram_dict(words):
    #Declares the dictionary
    anagrams = {}

    #For each line in the txt file
    for line in open(words):
        #Sort letters in each word alphabetically and assign to key
        key = "".join(sorted(line))
        #Calls append_anagram_dict to return defined dictionary
        append_anagram_dict(key.split(), anagrams, line)
    #sets the dictioary to only show anagrams in dictionary not all words whether there are anagrams or not
    anagrams = dict([(x,y) for x,y in anagrams.items() if len(y)>1])
    #Prints dictionary
    print(anagrams)

#Function to update the dictionary with each keys and values
def append_anagram_dict(words, anagrams, line):
    #Declares values list to hold anagrams
    values = []

    #For each key in txt file
    for key in words:
        #If key is already in dictionary
        if key in anagrams:
            #Adds current word to other word in list (that are anagrams)
            values.append(line.strip())
            #Adds list of anagrams to dictionary of anagrams
            anagrams[key.strip()] += values
        #Else add only current word
        else:
            #Adds current word to list
            values.append(line.strip())
            #Adds list of anagrams to dictionary of anagrams
            anagrams[key.strip()] = values

#Calls make_anagram_dict function with txt file
make_anagram_dict("words.txt")
