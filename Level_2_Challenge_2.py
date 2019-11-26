# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters¶

def paper_doll(input_word):
    
    input_list = list(input_word)
    resultant_string = ''
    sb = []
    for item in input_list:
        sb.append(item)
        sb.append(item)
        sb.append(item)
    
    resultant_string = ''.join(sb)
    return resultant_string

    
print(paper_doll('bhaskar'))

