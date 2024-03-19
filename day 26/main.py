from random import randint
import pandas

numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]

name = "Leonardo"
letters_list = [letter for letter in name]

double_list = [n * 2 for n in range(1, 5)]

names = ["Alex", "Beth", "Leonardo"]

short_names = [name for name in names if len(name) < 5]
long_names = [name.upper() for name in names if len(name) > 4]

student_scores = {student: randint(1, 100) for student in names}
passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}
# print(passed_students)

student_dict = {
  "student": ["Alex", "Leonardo"],
  "score": [53, 75],
}


student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
for (index, row) in student_data_frame.iterrows():
  print(row.score)