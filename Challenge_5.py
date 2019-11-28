""" How many connected components result after performing the following sequence of union operations on a set of 1010
items? 1–2 3–4 5–6 7–8 7–9 2–8 0–5 1–9 """


def dynamic_connectivity():
    # input_list = [(1, 2), (3, 4), (5, 6), (7, 8), (7, 9), (2, 8), (0, 5), (1, 9)]
    input_list = [(1, 2), (4, 5)]
    x = input_list[0][0]
    print(x)
    y = input_list[0][1]
    print(y)
    connections = 0
    total = []
    for item in input_list:
        if (item[0] == x + 1 or item[0] == x - 1) or (item[0] == y + 1 or item[0] == y - 1) \
                or (item[1] == x + 1 or item[1] == x - 1) or (item[1] == y + 1 or item[1] == y - 1):
            connections += 1
            print('checked_in', connections)
        else:
            pass
        total.append(connections + 1)

    grand_total = len(total)
    print(total)
    print(grand_total)


dynamic_connectivity()
