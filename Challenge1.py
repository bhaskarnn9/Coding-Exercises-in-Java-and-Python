'''
Define a function called myfunc that takes in a string and returns a matching straing where every even letter is uppercase, and every odd letter
is lowercase. Assume that the incoming string only comntains letters, and don't worry about numbers, spaces or punctuation. The output string can
start with either an uppercase or lowercase letter, so long as letters alternate throughout the string
'''

def myfunc(string):
    char_count = 0
    sb = []
    matching_string = ''
    while char_count < len(string):
        if char_count % 2 == 0:
            sb.append(string[char_count].upper())
        else:
            sb.append(string[char_count].lower())
        char_count+=1
    return matching_string.join(sb)



print(myfunc('Anthropomorphism'))


