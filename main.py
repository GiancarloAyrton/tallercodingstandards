"""Student Grade Management System with validation and reporting."""

from typing import List


class Student:
    """Class representing a student and their academic records."""

    def __init__(self, student_id: str, name: str):
        """
        Initialize a student with ID and name.

        Args:
            student_id (str): The unique identifier for the student.
            name (str): The student's full name.

        Raises:
            ValueError: If ID or name is empty.
        """
        if not student_id.strip() or not name.strip():
            raise ValueError("Student ID and name must not be empty.")
        self.student_id = student_id.strip()
        self.name = name.strip()
        self.grades: List[float] = []
        self.average: float = 0.0
        self.letter_grade: str = "N/A"
        self.passed: bool = False
        self.honor_roll: bool = False

    def add_grade(self, grade: float):
        """
        Add a grade to the student's grade list.

        Args:
            grade (float): A number between 0 and 100.

        Raises:
            ValueError: If the grade is invalid.
        """
        if not isinstance(grade, (int, float)):
            raise ValueError("Grade must be a number.")
        if grade < 0 or grade > 100:
            raise ValueError("Grade must be between 0 and 100.")
        self.grades.append(float(grade))

    def calculate_average(self):
        """Calculate average grade and update letter grade, pass/fail, and honor roll."""
        if not self.grades:
            self.average = 0.0
        else:
            self.average = sum(self.grades) / len(self.grades)

        # Assign letter grade
        if self.average >= 90:
            self.letter_grade = "A"
        elif self.average >= 80:
            self.letter_grade = "B"
        elif self.average >= 70:
            self.letter_grade = "C"
        elif self.average >= 60:
            self.letter_grade = "D"
        else:
            self.letter_grade = "F"

        # Determine pass/fail
        self.passed = self.average >= 60

        # Determine honor roll status
        self.honor_roll = self.average >= 90

    def remove_grade_by_index(self, index: int):
        """
        Remove a grade by its index.

        Args:
            index (int): Position in the grade list.

        Raises:
            IndexError: If index is invalid.
        """
        if 0 <= index < len(self.grades):
            del self.grades[index]
        else:
            raise IndexError("Index out of bounds. Cannot remove grade.")

    def remove_grade_by_value(self, value: float):
        """
        Remove the first occurrence of a grade value.

        Args:
            value (float): Grade value to remove.

        Raises:
            ValueError: If the value does not exist in the list.
        """
        if value in self.grades:
            self.grades.remove(value)
        else:
            raise ValueError(f"Grade {value} not found in the list.")

    def generate_report(self) -> str:
        """Generate and return a formatted summary report for the student."""
        return (
            f"📋 Student Report\n"
            f"---------------------\n"
            f"ID            : {self.student_id}\n"
            f"Name          : {self.name}\n"
            f"Grades        : {self.grades}\n"
            f"Total Grades  : {len(self.grades)}\n"
            f"Average       : {self.average:.2f}\n"
            f"Letter Grade  : {self.letter_grade}\n"
            f"Passed        : {'Yes' if self.passed else 'No'}\n"
            f"Honor Roll    : {'Yes' if self.honor_roll else 'No'}\n"
        )


def demo_run():
    """Demonstration of system functionality with example student."""
    try:
        student = Student("S001", "Giancarlo Ortiz")
        student.add_grade(95.0)
        student.add_grade(87.5)
        student.add_grade(91.0)

        # Invalid grades
        try:
            student.add_grade("A+")
        except ValueError as e:
            print("Invalid grade input:", e)

        try:
            student.add_grade(120)
        except ValueError as e:
            print("Out of range grade:", e)

        student.calculate_average()

        try:
            student.remove_grade_by_index(10)
        except IndexError as e:
            print("Index error:", e)

        try:
            student.remove_grade_by_value(72.0)
        except ValueError as e:
            print("Value error:", e)

        print(student.generate_report())

    except ValueError as e:
        print("Student creation failed:", e)


if __name__ == "__main__":
    demo_run()
