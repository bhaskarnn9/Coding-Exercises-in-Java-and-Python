'''
write a function that takes a two-word string and returns True
if both words begin with same letter
'''

def same_letter_words(str_arg):
    string_split = str_arg.split()
    word1 = string_split[0]
    word2 = string_split[1]
    if word1[0].lower() == word2[0].lower():
        return True
    else:
        return False


print(same_letter_words('hello world'))