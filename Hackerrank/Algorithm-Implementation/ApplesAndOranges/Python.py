def countApplesAndOranges(s, t, a, b, apples, oranges):
    x = [0,0]
    for i in range(len(apples)):
        apples[i] += a
        if(apples[i] >= s and apples[i] <= t):
            x[0] += 1
    
    for j in range(len(oranges)):
        oranges[j]+= b
        if(oranges[j] >= s and oranges[j] <= t):
            x[1]+= 1
        
    print(x[0])
    print(x[1])
