def cyclic_shift_first(a: list):
#from beginning to end
    tmp = a[0]
    for i in range(len(a)-1):
        a[i] = a[i+1]
    a[len(a)-1] = tmp
    return a



def cyclic_shift_last(a: list):
#from end to beginning
    tmp = a[len(a)-1]
    for i in range(len(a)-2, -1, -1):
        a[i+1] = a[i]
    a[0] = tmp
    return a
