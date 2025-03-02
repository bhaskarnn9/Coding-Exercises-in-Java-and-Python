"""
211. Design Add and Search Words Data Structure

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.


Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation

WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
"""
import sys


class WordDictionary:

    def __init__(self):

        # Initialize your data structure here.
        self.children = [None] * 26
        self.isEndOfWord = False

    def addWord(self, word: str) -> None:

        # Adds a word into the data structure.
        curr = self

        for c in word:
            if curr.children[ord(c) - ord('a')] == None:
                curr.children[ord(c) - ord('a')] = WordDictionary()
            curr = curr.children[ord(c) - ord('a')]
        curr.isEndOfWord = True

    def search(self, word: str) -> bool:

        # Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        curr = self
        for i in range(len(word)):
            c = word[i]
            if c == '.':
                for ch in curr.children:
                    if ch is not None and ch.search(word[i + 1:]):
                        return True
                return False

            if curr.children[ord(c) - ord('a')] is None:
                print('alpha', c)
                print('returning false')
                return False
            curr = curr.children[ord(c) - ord('a')]

        print('curr is not None', curr is not None)
        print('curr.isEndOfWord', curr.isEndOfWord)
        return curr is not None and curr.isEndOfWord


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord('a')
obj.search('.')
obj.addWord('word')
print(obj.search('worn'))
obj.addWord("google")
obj.addWord("bad")
obj.addWord("dad")
obj.addWord("mad")
print(obj.search("pad"))
print(obj.search("bad"))
print(obj.search(".ad"))
print(obj.search("b.."))
print(obj.search("g..gle"))
