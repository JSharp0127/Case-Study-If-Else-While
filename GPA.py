"""
Name: John Sharp
Filename: GPA.py
Description: 
-ask for and accept a student's last name.
-quit processing student records if the last name entered is 'ZZZ'.
-ask for and accept a student's first name.
-ask for and accept the student's GPA as a float.
-test if the student's GPA is 3.5 or greater and, if so, print a message saying that the student has made the Dean's List.
-test if the student's GPA is 3.25 or greater and, if so, print a message saying that the studnet has made the Honor Roll.

"""
def main():
    program_run = True

    while program_run == True:
        student_name = input("What is the students name? (Enter ZZZ to exit application): ")
        if student_name  == 'ZZZ':
            program_run = False
            break
        gpa = input("Enter students GPA: ")
        try:
            gpa = float(gpa)
        except ValueError:
            print("Enter GPA as a numerical value")
            main()
        if gpa > 4 or gpa < 0:
            print("GPA must be between 0 and 4")
            main()
        if gpa >= 3.5:
            print(f"{student_name} has made the Dean's List")
        elif gpa >= 3.25:
            print(f"{student_name} has made the Honor Roll")
        else:
            print("The student's GPA was to low to meet the requirments")

if __name__ == "__main__":
    main()

