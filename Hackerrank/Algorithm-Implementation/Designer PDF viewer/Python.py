def designerPdfViewer(h, word):
    max = 0
    x = 0
    for i in (word):
        x = ord(i) - 97
        if(h[x] > max):
            max = h[x]
    return max*len(word)
