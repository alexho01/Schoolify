# main.py

from grades import GradeCalculator
from quiz import Quiz
from calculator import Calculator


def get_grades():
    """Prompt the user to input grades and return a list."""
    grades = []
    num_grades = int(input("Enter the number of grades: "))
    for i in range(num_grades):
        grade = float(input(f"Enter grade {i + 1}: "))
        grades.append(grade)
    return grades


def run_grade_calculator():
    """Runs the grade calculator system."""
    print("Smart Grade Calculator")
    grades = get_grades()
    calculator = GradeCalculator(grades)

    if input("Drop the lowest grade? (yes/no): ").lower() == "yes":
        calculator.drop_lowest_grade()

    extra_credit = float(input("Enter extra credit points per grade (0 if none): "))
    calculator.apply_extra_credit(extra_credit)

    use_weights = input("Use weighted grading? (yes/no): ").lower() == "yes"
    weights = None
    if use_weights:
        weights = [float(input(f"Enter weight for grade {i + 1}: ")) for i in range(len(calculator.grades))]

    final_grade = calculator.compute_final_grade(use_weights, weights)
    letter_grade = calculator.convert_to_letter(final_grade)

    print(f"Final Grade: {final_grade:.2f} ({letter_grade})")


def run_quiz_app():
    """Runs the quiz application."""
    subject = input("Enter the subject for the quiz: ")
    quiz = Quiz(subject)

    num_questions = int(input("How many questions would you like to add? "))
    for _ in range(num_questions):
        question = input("Enter the question: ")
        q_type = input("Is this multiple-choice? (yes/no): ").lower()

        if q_type == "yes":
            options = [input(f"Option {i + 1}: ") for i in range(4)]
            correct_answer = input("Enter the correct answer: ")
        else:
            options = None
            correct_answer = input("Enter the correct answer: ")

        quiz.add_question(question, options if options else correct_answer, correct_answer)

    quiz.take_quiz()


def run_calculator():
    """Runs the calculator app."""
    calculator = Calculator()

    # Prompt user to choose radians or degrees
    angle_mode = input(
        "Would you like to use radians or degrees for trigonometric functions? (Enter 'radians' or 'degrees'): ")
    calculator.set_angle_mode(angle_mode)

    while True:
        print("\nCalculator: Enter a mathematical expression, or type 'exit' to quit.")
        expression = input("Enter calculation: ")
        if expression.lower() == 'exit':
            print("Exiting calculator.")
            break
        else:
            result = calculator.evaluate_expression(expression)
            if "Error" in str(result):
                print(result)  # Print the error message
                print(
                    "Please check your expression. For example, ensure multiplication (*) is used between numbers and parentheses.")
            else:
                print(f"Result: {result}")


def main():
    """Main interface for selecting between grade calculator, quiz app, and calculator."""
    while True:
        print("\nMain Menu")
        print("1. Smart Grade Calculator")
        print("2. Subject-Based Quiz App")
        print("3. Calculator")
        print("4. Exit")

        choice = input("Select an option: ")
        if choice == "1":
            run_grade_calculator()
        elif choice == "2":
            run_quiz_app()
        elif choice == "3":
            run_calculator()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
