PASS_SCORE = 60 
EXCELLENT_SCORE = 85

while True :
    student_count = int(input("Number Of Studdent: "))
    if student_count <= 1:
        print ("Invalid Student Count")
    else :
        break

total_score = 0
passed_score = 0
excellent_score = 0
highest_score = 0

for j in range (1,student_count + 1):
    print("Student: " , j)

    while True :
        score = int(input("Enter Score: "))
        if score < 0 or score > 100:
            print("Invalid Score ")
        else :
            break

    total_score += score

    if score >= PASS_SCORE:
        passed_score += 1

    if score >= EXCELLENT_SCORE:
        excellent_score += 1

    if score >= highest_score:
        highest_score = score

average = total_score / student_count

print("Total Score: ", total_score)
print("Average Score: ", round(average, 2))
print("Passed: ", passed_score)
print("Excellent count: ", excellent_score)
print("Highest Score: ", highest_score)