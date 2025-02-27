"""
Given a word, find the length of non-repeating longest character sequence in the word.
Example:
Input: "aabbcc"
Output: 2 ("ab" or "bc)

Input: "aabccaabcd"
Output: 4 ("abcd")
"""


def longest_non_repeating_char_sequence(word: str):
    maxi = 0
    maxi_word = ""
    for i in range(len(word)):
        for j in range(i+1, len(word)+1): # sliding window

            temp_word = word[i:j] # get the sliced word
            # print('i:', i, 'j:', j, 'temp_word:', temp_word)
            if len(temp_word) == len(set(temp_word)): # if len of word is equal to len of unique chars in it
                maxi = max(maxi, len(set(temp_word)))
                if len(maxi_word) < len(temp_word): # optional: store the sequence too
                    maxi_word = temp_word

    print('\n')
    print(maxi_word)
    print(maxi)

longest_non_repeating_char_sequence("aabbcc")
longest_non_repeating_char_sequence("aabccdaabcd")


