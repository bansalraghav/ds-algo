int designerPdfViewer(vector<int> h, string word) {
    int max = 0,x=0;
    for(char i = 0; i<word.size(); i++){
        x = int(word[i]) - 97;
        if(h[x] > max){
            max = h[x];
        }
    }
    return max*word.size();
}
