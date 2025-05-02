#Kevin Beaghan 3/31/2025
#Week 11 Lab - Opening files and extracting and organizing data into new files

def final_file(grades):
    newFile = "grades.txt"
    with open(newFile, 'w', newline='') as f:
        for row in grades:
            f.write(','.join(map(str, row)) + '\n')
    print(f"Grades saved to {newFile}.")

def combinedata(students, scores):
    grades = [["Student ID", "Name", "Total Scores", "Sum of All Scores", "Score Average"]]
    for student in students:
        student_id = student["id"]
        student_name = student["name"]
        if student_id in scores:
            total_scores = len(scores[student_id])
            sum_scores = sum(scores[student_id])
            avg_score = round(sum_scores / total_scores, 2) if total_scores > 0 else 0
        grades.append([student_id, student_name, total_scores, sum_scores, avg_score])
    return grades

def extractscoredata(file):
    scores = {}
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines[1:]:
            student_id, assignment, score = line.strip().split(',')
            score = int(score)
            if student_id not in scores:
                scores[student_id] = []
            scores[student_id].append(score)
    return scores

def extractstudentdata(file):
    students = []
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines[1:]:
            student_id, name = line.strip().split(',')
            students.append({"id": student_id, "name": name})
    return students

def main():
    students = extractstudentdata(input("Please enter the file name containing student data:"))
    scores = extractscoredata(input("Please enter the file name containing score data:"))
    grades = combinedata(students, scores)
    final_file(grades)

if __name__ == "__main__":
    main()