# Given an integer n, return True if n is within 10 of either 100 or 200

def almost_there(input_int):
    check_1 = 100
    check_2 = 200

    if input_int > check_1-10 and input_int < check_1+10:
        return True
    elif input_int > check_2-10 and input_int < check_2+10:
        return True
    else:
        return False

print(almost_there(210))
