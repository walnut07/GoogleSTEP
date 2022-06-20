# How to run:
# python3 findAnagram2.py

# ---- The description of this program ---- #
# findAnagram2-desc.md

# Count every character in a word in a dictionary.
def countStringOfWordInDictionary(original_dictionary):
    new_dictionary = [ dict() for _ in range(len(original_dictionary)) ] # Create an empty list that has nested dictionaries 

    for i in range(len(original_dictionary)): # Iterate thru all the words.
        for string in original_dictionary[i]: # Iterate thru all the characters in a word.
            if string not in new_dictionary[i]:
                new_dictionary[i][string] = 1
            else:
                new_dictionary[i][string] += 1

    return new_dictionary

def countStringOfWord(original_word): # Count every character in a word you want to search anagrams of.
    new_word = {}

    for string in original_word:
        if string not in new_word:
            new_word[string] = 1
        else:
            new_word[string] += 1

    return new_word

def extractSubsetAnagramsOfWordFromDict(new_dictionary, new_word): # Extract subset anagrams of the word you want to search.

    subsetAnagrams = []

    for i in range(len(new_dictionary)):            # Iterate thru all the words in the dictionary
        isSubset = True
        for charactor, count in new_dictionary[i].items():
            if charactor not in new_word: 
                isSubset = False                   
            else: 
                if new_dictionary[i][charactor] > count: # If the word in a dictionary has more same characters than the word you wanna search anagrams of,
                    isSubset = False                  # the word in a dictionary isn't a subset anagram.
        if isSubset:                                 # If the isSubset keeps to be True, 
            subsetAnagrams.append("".join(new_dictionary[i].keys())) # append the word into |subsetAnagrams|

    return subsetAnagrams

def calculateScores(subsetAnagrams):
    SCORES = [1, 3, 2, 2, 1, 3, 3, 1, 1, 4, 4, 2, 2, 1, 1, 3, 4, 1, 1, 1, 2, 3, 3, 4, 3, 4]
    scores = []

    for anagram in subsetAnagrams:
        score = 0
        for string in list(anagram):
            score += SCORES[ord(string) - ord('a')]
        scores.append(score)
    return scores

def getHighestScoreAnagram(subsetAnagrams, scores): # output the subset-anagram whose score is the highest
    d = {}

    for i in range(len(subsetAnagrams)):
        d[scores[i]] = subsetAnagrams[i]

    return d[max(d)]


original_dictionary = []
with open('words.txt') as f:
    lines = f.readlines()
    for l in lines:
        original_dictionary.append(l.rstrip("\n"))

new_dictionary = countStringOfWordInDictionary(original_dictionary)

word = input() # the word you wanna search anagrams of.
new_word = countStringOfWord(word)
subsetAnagrams = extractSubsetAnagramsOfWordFromDict(new_dictionary, new_word)
scores = calculateScores(subsetAnagrams)
answer = getHighestScoreAnagram(subsetAnagrams, scores)
print(answer)

# ------------------- #

# How to calculate scores:
# python3 score_checker.py small.txt small_answer.txt
# python3 score_checker.py medium.txt medium_answer.txt
# python3 score_checker.py large.txt large_answer.txt

# ---- small.txt ---- #

"""
with open('small.txt') as f_txt:
    with open('small_answer.txt','w') as f_ans:
        lines = f_txt.readlines()
        for l in lines:
            new_dictionary = countStringOfWordInDictionary(original_dictionary)
            word = l.rstrip("\n")
            new_word = countStringOfWord(word)
            subsetAnagrams = extractSubsetAnagramsOfWordFromDict(new_dictionary, new_word)
            scores = calculateScores(subsetAnagrams)
            answer = getHighestScoreAnagram(subsetAnagrams, scores)
            f_ans.write(answer+"\n")
f_ans.close()
f_txt.close()
# ---- medium.txt ---- #
with open('medium.txt') as f_txt:
    with open('medium_answer.txt','w') as f_ans:
        lines = f_txt.readlines()
        for l in lines:
            new_dictionary = countStringOfWordInDictionary(original_dictionary)
            word = l.rstrip("\n")
            new_word = countStringOfWord(word)
            subsetAnagrams = extractSubsetAnagramsOfWordFromDict(new_dictionary, new_word)
            scores = calculateScores(subsetAnagrams)
            answer = getHighestScoreAnagram(subsetAnagrams, scores)
            f_ans.write(answer+"\n")
f_ans.close()
f_txt.close()
# ----- large.txt ----- #
with open('large.txt') as f_txt:
    with open('large_answer.txt','w') as f_ans:
        lines = f_txt.readlines()
        for l in lines:
            new_dictionary = countStringOfWordInDictionary(original_dictionary)
            word = l.rstrip("\n")
            new_word = countStringOfWord(word)
            subsetAnagrams = extractSubsetAnagramsOfWordFromDict(new_dictionary, new_word)
            scores = calculateScores(subsetAnagrams)
            answer = getHighestScoreAnagram(subsetAnagrams, scores)
            f_ans.write(answer+"\n")
f_ans.close()
f_txt.close()
"""