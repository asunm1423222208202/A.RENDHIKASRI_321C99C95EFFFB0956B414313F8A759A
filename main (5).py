"""Implement a function called sort_students that takes a list of student objects as input and sorts the list based on their CGPA in descending order."""


class student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa

def sort_students(student_list):
  #Sort the list of students in descending order of CGPA
  sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
  return sorted_students


#Example usage:
students = [
    student("Rendhika", "A123", 7.8),
    student("Loshini", "A124", 8.9),
    student("Hari", "A125", 9.1),
    student("Ramu", "A126", 9.9),
]
sorted_students = sort_students(students)

#Print the sort list or students
for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name, student.roll_number, student.cgpa))