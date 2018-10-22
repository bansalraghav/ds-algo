def utopianTree(n):
    if(n == 0):
        return 1
    h = 1
    for i in range(1, n+1):
        if(i%2 != 0):
            h = h*2
        else:
            h = h+1
    return h
