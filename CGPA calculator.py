print("This is a CGPA calculator app, fill in the appropriate details to get your correct GPA score")
courses_offered = int(input("How many courses do you offer?: "))
while int(courses_offered)>9 or int(courses_offered)<7:
   courses_offered = input("You can only offer a maximum of 9 and minimum of 7 courses, try again: ")
else:
   course_unit = []
   course_grade = []
   course_unit = [int(item) for item in input("Write out the unit for each courses(eg;1,2,3,4): ").split(",")]
   while len(course_unit) is not int(courses_offered):
      course_unit = [int(item) for item in input("Number of course unit must be same as number of courses offered, try again: ").split(",")]
   else:
      total_load_unit = sum(course_unit)
      course_grade = [int(item) for item in input("Write out the grade for each courses(eg;1,2,3,4): ").split(",")]
      while len(course_grade) is not int(courses_offered):
         course_grade = [int(item) for item in input("Number of course grade must be same as number of courses offered,try again: ").split(",")]
      else:
         credit_point = []
         for (item1, item2) in zip(course_unit, course_grade):
            credit_point.append(item1 * item2)
         total_credit_point = sum(credit_point)
         gpa = round((total_credit_point/total_load_unit),2)
         print("Your GPA is " + str(gpa))