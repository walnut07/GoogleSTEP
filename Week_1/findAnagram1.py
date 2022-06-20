# The time complexity 

# How to run
# python3 findAnagram1.py


# ----- define functions ----- #
import re

def sortWordsInDictionary(original_dictionary): 
    # returns a hashmap whose keys are an alphabetically sorted words and values are original words ex) {"aet" : "eat", "tea"} 
    
    dictionary = {}

    for original_word in original_dictionary:
        sorted_word = "".join(sorted(original_word))
        if sorted_word in dictionary:
            dictionary[sorted_word].append(original_word)
        else:
            dictionary[sorted_word] = [ original_word ]

    new_dictionary = dict(sorted(dictionary.items())) # sort words alphabetically
    return new_dictionary

def sortWordYouWannaSearch(word): 
    new_word = "".join(sorted(word)) # ex: "eat" → "aet"
    return new_word

def findAnagramsByBinarySearch(new_dictionary, new_word): # returns one or mutiple anagram(s)
    new_dict_keys = list( new_dictionary.keys() ) 
    right = len(new_dict_keys) - 1
    left = 0

    while left <= right:
        mid = ( right + left ) // 2
        if new_dict_keys[mid] == new_word:
            anagrams = new_dictionary[new_dict_keys[mid]] # Once found out the position of the sorted word you wanna search anagrams of in a dictionary, 
            return anagrams # return the values - in another word, anagrams.
        elif new_dict_keys[mid] > new_word:
            right = mid - 1
        elif new_dict_keys[mid] < new_word:
            left = mid + 1
    
    return False # returns false if no anagram is found

# ----------------------- #


# import the dictionary file
original_dictionary = []
with open('words.txt') as f:
    lines = f.readlines()
    for l in lines:
        original_dictionary.append(l.rstrip("\n"))

new_dictionary = sortWordsInDictionary(original_dictionary)  

word = input("Enter an Alphabetical Word! ") 
regex = re.search('[0-9/亜-熙ぁ-んァ-ヶ]',word) 

while regex != None: # ban Japanese letters or numbers by using regex
    word = input("Enter an Alphabetical Word! ")
    regex = re.search('[0-9/亜-熙ぁ-んァ-ヶ]',word)

new_word = sortWordYouWannaSearch(word)
anagrams = findAnagramsByBinarySearch(new_dictionary, new_word)

if anagrams == False:
    print("-------")
    print("NO_ANAGRAM_FOUND")
    print("-------")
else:
    print("-------")
    print("Here's what found: ")
    for anagram in anagrams:
        print(anagram)
    print("-------")
