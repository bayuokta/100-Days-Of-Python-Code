student_heights = input("Input a list of student heights ").split()
len_student = 0
total_height = 0

for i in range(0, len(student_heights)):
    student_heights[i] = int(student_heights[i])

for height in student_heights:
    total_height += height
    len_student += 1

y = total_height / len_student

print(y)
