def gradingStudents(grades):
    # Write your code here
    newGrades=[]
    for grade in grades:
        if grade <38:
            newGrades.append(grade)
        elif (grade+1)%5==0:
            newGrades.append(grade+1)
        elif (grade+2)%5==0:
            newGrades.append(grade+2)
        else:
            newGrades.append(grade)
    return newGrades
