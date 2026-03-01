#Count how many vowels are in a given string.
'''
Here is a clean, structured explanation you can add as a comment for future reference:

Goal: Count the total number of vowels present in a given string.

Vowels Considered: a, e, i, o, u (including uppercase: A, E, I, O, U).

Initialize Counter: Start a variable (e.g., count) with value 0 to store the number of vowels found.

Traverse the String: Visit each character one by one using a loop.

Condition Check: For each character, check whether it belongs to the vowel group.

Increment Logic: If the character is a vowel, increase the counter by 1.

Ignore Others: If the character is not a vowel (space, consonant, symbol, digit), skip it and continue.

Final Step: After the loop completes, the counter contains the total number of vowels.

Key Concept: This problem demonstrates string traversal, membership testing (in), and the counter/accumulator pattern.

Important Note: Avoid using break, as the entire string must be checked.

This explanation is clean, logical, and good for documentation or interview revision.
'''
_Name_= " Hello Bro! my name is Nikhil Ranjan, Whats your name."
ch='aeiouAEIOU'
char=0
for ch in _Name_ :
    if ch in ("aeiouAEIOU"):
        char=char+1
    
print(char)