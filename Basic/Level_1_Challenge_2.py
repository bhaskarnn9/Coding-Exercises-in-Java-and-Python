# Given a sentence return a sentence with the characters reversed in each word

def reverse_words_in_sentence(input_sentence):
    word_list = []
    word_list_reversed = []
    word_list = input_sentence.split(' ')
    reveresed_word_sentence = ''
    print(word_list)
    for word in word_list:
        reversed_word = ''
        last_char_index = len(word)-1
        sb = []
        while last_char_index > 0:
            sb.append(word[last_char_index])
            last_char_index -= 1

        sb.append(word[0])
        reversed_word = reversed_word.join(sb)
        word_list_reversed.append(reversed_word)
        
    reveresed_word_sentence = ' '.join(item for item in word_list_reversed)
    return reveresed_word_sentence


print(reverse_words_in_sentence('hi this is Bhaskar here trying to crack the challenge'))

