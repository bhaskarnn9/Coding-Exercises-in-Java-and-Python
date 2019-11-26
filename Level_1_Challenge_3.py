# Given a sentence, return a sentence with the words reversed

def reverse_words_in_sentence(input_sentence):
    sentence_with_words_reversed = ''
    word_list = []
    word_list = input_sentence.split(' ')
    reversed_word_list = []
    last_word_index = len(word_list) - 1

    x = 0
    while last_word_index > x:
        reversed_word_list.append(word_list[last_word_index])
        last_word_index -= 1

    reversed_word_list.append(word_list[0])
    sentence_with_words_reversed = ' '.join(item for item in reversed_word_list)
    return sentence_with_words_reversed


result = reverse_words_in_sentence('Hi This is Bhaskar')
print(result)

