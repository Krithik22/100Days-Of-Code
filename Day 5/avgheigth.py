student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    # sum+=student_heights[n]
    # count+=1

count=0
sum=0
for height in student_heights:
    sum+=height
    count+=1
avg=sum/count
print(round(avg))