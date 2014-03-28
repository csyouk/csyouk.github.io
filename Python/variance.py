grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print grade
        

def grades_sum(grades):
    total = 0
    for grade in grades: 
        total += grade
    return total
    
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / len(grades)
    return average

#print grades_average(grades)

def grades_variance(scores,average):
    sum=0
    num=len(scores)
    for grade in scores:
        Deviation=grade-average
        variance = Deviation**2
        sum += variance
    return sum/num

print grades_variance(grades,grades_average(grades))








