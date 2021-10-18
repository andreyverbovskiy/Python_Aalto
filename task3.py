def determine_grade_limit(max_points,passing_percentage):

  arr = []

  min_grade = (max_points*passing_percentage)/100

  grade_diff = (max_points-min_grade)/5

  grade2 = min_grade + grade_diff

  grade3 = grade2 + grade_diff

  grade4 = grade3 + grade_diff

  grade5 = grade4 + grade_diff

  arr.append(min_grade)
  arr.append(grade2)
  arr.append(grade3)
  arr.append(grade4)
  arr.append(grade5)

  return arr



def grade_points(exam_points,grade_limit):
  
  if(exam_points < grade_limit[0]):
    return 0 
  elif(grade_limit[0] <= exam_points < grade_limit[1]):
    return 1
  elif(grade_limit[1] <= exam_points < grade_limit[2]):
    return 2
  elif(grade_limit[2] <= exam_points < grade_limit[3]):
    return 3
  elif(grade_limit[3] <= exam_points < grade_limit[4]):
    return 4
  elif(grade_limit[4] <= exam_points):
    return 5



def main():

  grades = []

  max_points = float(input('Enter the maximum points of the exam: \n '))

  pass_percentage = int(input('Enter the passing percentage of the exam: \n '))

  inp = 1

  while(inp != ""):
    inp = input("Enter the exam points of the students. Stop with empty line: \n")
    if(inp != ''):
      grades.append(float(inp))
    else:
      pass

  lim = determine_grade_limit(max_points, pass_percentage)

  print("Points Grades")
  for x in (grades):
    print(x,'   ', grade_points(x,lim),'\n')


main()
