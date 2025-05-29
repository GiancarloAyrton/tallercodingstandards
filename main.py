"""Student Grade Management System"""

from typing import List


class Student:
    """A class representing a student with grades."""

    def __init__(self, student_id: str, name: str):
        """
        Initialize a student with ID and name.

        Args:
            student_id (str): Unique identifier for the student.
            name (str): Name of the student.

        Raises:
            ValueError: If ID or name is empty.
        """
        if not student_id.strip() or not name.strip():
            raise ValueError("Student ID and name must not be empty.")

        self.student_id = student_id.strip()
        self.name = name.strip()
        self.grades: List[float] = []
        self.average = 0.0
        self.letter_grade = "N/A"
        self.passed = False

    def add_grade(self, grade: float):
        """
        Add a numeric grade to the student's record.

        Args:
            grade (float): Grade to add (0–100).

        Raises:
            ValueError: If grade is invalid.
        """
        if not isinstance(grade, (int, float)):
            raise ValueError("Grade must be a number.")
        if grade < 0 or grade > 100:
            raise ValueError("Grade must be between 0 and 100.")
        self.grades.append(float(grade))

    def calculate_average(self):
        """Calculate the average of all grades."""
        if not self.grades:
            self.average = 0.0
        else:
            self.average = sum(self.grades) / len(self.grades)
        self._assign_letter_grade()
        self._determine_pass_status()

    def _assign_letter_grade(self):
        """Assign a letter grade based on the average."""
        avg = self.average
        if avg >= 90:
            self.letter_grade = "A"
        elif avg >= 80:
            self.letter_grade = "B"
        elif avg >= 70:
            self.letter_grade = "C"
        elif avg >= 60:
            self.letter_grade = "D"
        else:
            self.letter_grade = "F"

    def _determine_pass_status(self):
        """Determine if the student has passed based on average."""
        self.passed = self.average >= 60

    def report(self):
        """Print a detailed report of the student's performance."""
        print(f"Student ID   : {self.student_id}")
        print(f"Name         : {self.name}")
        print(f"Grades       : {self.grades}")
        print(f"Average      : {self.average:.2f}")
        print(f"Letter Grade : {self.letter_grade}")
        print(f"Passed       : {'YES' if self.passed else 'NO'}")


def demo_run():
    """Demonstrate system functionality with sample inputs."""
    try:
        student_a = Student("001", "Alice")
        student_a.add_grade(95.0)
        student_a.add_grade(88.5)
        student_a.add_grade(73)
        # Invalid entries (handled gracefully)
        try:
            student_a.add_grade("A+")
        except ValueError as err:
            print("Error adding grade:", err)
        try:
            student_a.add_grade(-10)
        except ValueError as err:
            print("Error adding grade:", err)

        student_a.calculate_average()
        student_a.report()
    except ValueError as err:
        print("Error creating student:", err)


if __name__ == "__main__":
    demo_run()
