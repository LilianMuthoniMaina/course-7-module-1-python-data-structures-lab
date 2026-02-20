# This module contains operations related to sets.

def unique_majors(student_list):
    majors= set()
    for student in student_list:
        majors.add(student[2])
    return majors