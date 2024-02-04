exam_grades = [83, 85, 72, 65, 76, 90, 79, 88, 93, 70, 67, 80]

print (len(exam_grades), "Students took the exam.")
print("The highest grade was a", max(exam_grades))
print("The lowest grade was a", min(exam_grades))
print("The average grade for the exam was a", sum(exam_grades)/len(exam_grades))

attendance_day1 = {'Mary', 'Jake', 'Sam', 'Alex', 'Percy', 'Jessica', 'Trent', 'Mahmoud'}
attendance_day2 = {'Jake', 'Sam', 'Alex', 'Percy', 'Mahmoud', 'Trent', 'Caleb', 'Zayne'}

total_attendance = attendance_day1.union(attendance_day2)

print(len(total_attendance), "students attended the class.")

print(attendance_day1.intersection(attendance_day2), "attended both class days.")
print(attendance_day1.symmetric_difference(attendance_day2), "attended one class day.")