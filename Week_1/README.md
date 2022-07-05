# Program description of `findAnagram1.py` and `findAnagram2.py`

## `findAnagram1.py`
`findAnagram1.py` returns all the anagrams of the word you input.

### How to run
Put the command below and input any English word.
```
python3 findAnagram1.py
```

**The program has five processes**
1. Create a new dictionary whose data type is a hashmap. 
 - Its key is a sorted word and value is the original word.  ex: {"aet" : "eat", "tea"} 
 - The words are sorted by the key.
2. Sort the word that you input. ex: "eat" → "aet"
3. Find the sorted input word in the new dictionary by Binary Search.

## `findAnagram2.py`

### Summary 
`findAnagram2.py` finds one or multiple word(s) that can be consisted of the characters of the word you input. It eventually returns a word that has the highest score among them.

>e.g., it should find ["at", "cat"] if you input "tac" and finally returns "cat".

### How to run
Put the command below and input any English word.
```
python3 findAnagram2.py
```

<br>

**The program has five processes**
1. Count every character in a word in a dictionary.

2. Count every character in a word that you wanna search.

3. Extract words from the dictionary by checking if each character of the word is in a word in a dictionary and if the word you wanna search has more or equivalent number of the character when the word you wanna search and a word in a dictionary have the same character.

4. Calculate the scores of extracted words.

5. Cutputs the word that has the highest score.
