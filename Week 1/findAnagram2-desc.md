# **The program description of findAnagram2.py** 

## Summary of the feature
This program finds one or multiple word(s) that can be consisted of the characters of the word you input. It eventually returns a word that has the highest score among them.

>e.g., it should find ["at", "cat"] if you input "tac" and finally returns "cat".

<br>

## The program has five processes
1. Count every character in a word in a dictionary.

2. Count every character in a word that you wanna search.

3. Extract words from the dictionary by checking if each character of the word is in a word in a dictionary and if the word you wanna search has more or equivalent number of the character when the word you wanna search and a word in a dictionary have the same character.

4. Calculate the scores of extracted words.

5. Cutputs the word that has the highest score.

***

## The issue so far not fixed
The third function `extractSubsetAnagramsOfWordFromDic` does not work as expected. 

I expect it to return all the words that can be consisted of the characters of the word you wanna search.
> e.g., it should return ["at", "cat"] if an user input "tac".

However, it returns words that have characters not appeared in the word you wanna search.
> e.g., it returns ['outlawing', 'untowardly', 'walnut', 'walnuts', 'wanderlust', 'wastefuln', 'watchfulnes', 'wrathfulnes'] if an user input "walnut".

According to my analysis, part of the code in `extractSubsetAnagramsOfWordFromDict` seems not working properly.

    if string not in new_dictionary[i]: 
        isSubset = False
    if new_dictionary[i][string] > count:
        isSubset = False    

Could you think of some reason why this program returns words that have characters not appeared in the word an user inout?

Many thanks in advance.