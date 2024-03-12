# Write a function that capitalizes the first and fourth letters of the input (assuming input is at least 5 characters
# long)

def cap_1_4_letter(str_input):
    x = 0
    sb = []
    matching_string = ''
    while x < len(str_input):
        if x == 0 or x == 3:
            sb.append(str_input[x].upper())
        else:
            sb.append(str_input[x].lower())
        x+=1
    return matching_string.join(sb)


print(cap_1_4_letter('macdonald'))
