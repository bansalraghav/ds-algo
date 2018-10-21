void countApplesAndOranges(int s, int t, int a, int b, vector<int> apples, vector<int> oranges) {
    int c1 = 0, c2 = 0;
    for(int i = 0; i< apples.size(); i++){
        apples[i] += a;
        if(apples[i] >= s && apples[i] <= t){
            c1 += 1;
        }        
    }
    for(int i = 0; i< oranges.size(); i++){
        oranges[i] += b;
        if(oranges[i] >= s && oranges[i] <= t){
            c2 += 1;
        }
    }
    cout<<c1<<endl<<c2;
}
