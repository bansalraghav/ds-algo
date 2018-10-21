vector<int> gradingStudents(vector<int> grades) {
    /*
     * Write your code here.
     */
    int x = 0;
    for(auto i = grades.begin(); i != grades.end(); i++){
        if(*i > 37){
            x = *i/5;
            if((*i - x*5) >2){
                *i = (x+1)*5; 
            }
        }
    }
    return grades;
}
