def calculate_total_marks(marks):
    return sum(marks)

def calculate_percentage(total_marks, max_marks_per_subject,marks):
    total_max_marks = max_marks_per_subject * len(marks)
    percentage = (total_marks / total_max_marks) * 100
    return round(percentage, 2)

def is_passed(percentage, passing_percentage):
    return percentage >= passing_percentage

def print_report_card(name, marks, total_marks, percentage, passing_percentage):
    print("Student Name:", name)
    print("Total Marks:", total_marks)
    print("Percentage:", percentage, "%")
    if is_passed(percentage, passing_percentage):
        print("Result: Pass")
    else:
        print("Result: Fail")

def main():
    max_marks_per_subject = 100
    num_subjects = 3
    passing_percentage = 40

    name = input("Enter student name: ")

    marks = []
    for i in range(num_subjects):
        mark = int(input("Enter marks for Subject {}: ".format(i + 1)))
        marks.append(mark)

    total_marks = calculate_total_marks(marks)
    percentage = calculate_percentage(total_marks, max_marks_per_subject,marks)

    print("\n*** Report Card ***")
    print_report_card(name, marks, total_marks, percentage, passing_percentage)

if __name__ == "__main__":
    main()
