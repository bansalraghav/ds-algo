string kangaroo(int x1, int v1, int x2, int v2) {
    float y = 0;
    y = (x1 - x2 + 0.0)/(v2 - v1);
    if(y - (int)y == 0 && y>=0){
        return "YES";
    }
    else{
        return "NO";
    }
}
