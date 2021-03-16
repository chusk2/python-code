"""HackerLand University has the following grading policy:

Every student receives a  in the inclusive range from  to .
Any  less than  is a failing grade.
Sam is a professor at the university and likes to round each student's  according to these rules:

If the difference between the grade and the next multiple of 5 is less than 3,
round  up to the next multiple of 5.
If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.
Examples

 round to  (85 - 84 is less than 3)
 do not round (result is less than 40)
 do not round (60 - 57 is 3 or higher)
Given the initial value of  for each of Sam's  students, write code to automate the rounding process."""

def gradingStudents(grades):
    
    rounded_grades = []
    for grade in grades[1:] :

        if grade < 38 :
            rounded_grades.append(grade)
        
        elif grade >= 38 :
            
            next_multiple5 = grade
            while (next_multiple5 % 5) != 0 :
                next_multiple5 += 1
            
            if next_multiple5 - grade < 3 :

                grade = next_multiple5
                rounded_grades.append(grade)
            
            else :
                rounded_grades.append(grade)

    for grade in rounded_grades :
        print(grade)
    
grades=[4,73,67,38,33]
gradingStudents(grades)


            