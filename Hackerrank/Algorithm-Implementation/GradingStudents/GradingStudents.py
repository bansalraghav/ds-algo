def gradingStudents(grades):
    # Write your code here.
    for i in range(len(grades)):
        if grades[i] > 37:
            x = (grades[i]//5) 
            if ((grades[i] - x*5) > 2):
                grades[i] = 5*(x+1)
    return grades
