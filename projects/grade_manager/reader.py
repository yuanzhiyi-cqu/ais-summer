import csv


def read_scores(filename):
    students = []

    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            name = row["name"]
            score = float(row["score"])
            students.append({"name": name, "score": score})

    return students


def analyze_scores(students):
    scores = []

    for student in students:
        scores.append(student["score"])

    average_score = sum(scores) / len(scores)
    max_score = max(scores)
    min_score = min(scores)

    print("Average score:", average_score)
    print("Max score:", max_score)
    print("Min score:", min_score)


def main():
    students = read_scores("projects/grade_manager/data/scores.csv")

    print("Students:")
    print(students)

    analyze_scores(students)


main()