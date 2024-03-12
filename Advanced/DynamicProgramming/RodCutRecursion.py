inp = [0, 3, 7, 9, 12]
cuts = 4

def rod_cut(l, inp):
    
    if l == 0:
        return 0
    
    max_revenue = 0
    
    for i in range(l-1):
        revenue = inp[l-i] + rod_cut(i, inp)
        max_revenue = max(revenue, max_revenue)
    
    return max_revenue

print(rod_cut(cuts, inp))