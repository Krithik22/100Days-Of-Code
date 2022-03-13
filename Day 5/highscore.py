student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# max_score=10
# for x in range(0, len(student_scores)):
#     if student_scores[x]>max_score:
#         max_score=student_scores[x]
#     else:
#         max_score=max_score
max_score=0
for score in student_scores:
    if score>max_score:
        max_score=score
print("The highest score in the class is:",max_score)