#
# text= "Angela"
#
# new_list = [n for n in text]
# print(new_list)
#
# """       new_list_1 = [new_item for item in names if test]      """
# """       new_dict_1 = [key:value for key, value in names.items() if test]"""
#
# names = ["Alex", "Beth", "Carolina", "Dave", "Eleanor","Freddie"]
#
# long = [name.upper() for name in names if len(name) > 5]
# print(long)
#
# import random
#
# students_scores = {student:random.randint(1,100) for student in names}
# print(students_scores)
# passes_students = {student:score for student, score in students_scores.items() if score >= 60}
# print(passes_students)
import pandas

# import pandas
#
# students = {
#     "students": ["Angela", "Beth", "Carolina", "Dave", "Eleanor", "Freddie"],
#     "score": [56, 57, 58, 59, 60, 61]
# }
#
# students_data = pandas.DataFrame(students)
# for (index,row) in students_data.iterrows():
#     if row.students == "Angela":
#         print(row.score)

nato = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for letters, row in nato.iterrows()}
print(nato_dict)

name = input("Write something to transform to phonetic dictionary").upper()
output = [nato_dict[letter] for letter in name]
print(output)