"""Module for managing student grades."""


class Student:
    """A class representing a student and their academic records."""

    def __init__(self, student_id, name):
        """Initialize a student with an ID and name."""
        self.student_id = student_id
        self.name = name
        self.grades = []
        self.is_passed = "NO"
        self.honor = "?"
        self.letter = "N/A"

    def add_grades(self, grade):
        """Add a numeric grade to the student's list."""
        if isinstance(grade, (int, float)):
            self.grades.append(grade)
        else:
            print(f"Ignored invalid grade: {grade}")

    def calc_average(self):
        """Calculate the average grade."""
        if not self.grades:
            print("No grades available to calculate average.")
            return 0
        average = sum(self.grades) / len(self.grades)
        # Determine letter grade
        if average >= 90:
            self.letter = "A"
        elif average >= 80:
            self.letter = "B"
        elif average >= 70:
            self.letter = "C"
        elif average >= 60:
            self.letter = "D"
        else:
            self.letter = "F"

        # Set pass/fail
        self.is_passed = "YES" if average >= 60 else "NO"
        return average

    def check_honor(self):
        """Determine if the student qualifies for honors."""
        if self.calc_average() >= 90:
            self.honor = "YES"
        else:
            self.honor = "NO"

    def delete_grade(self, index):
        """Delete a grade by index."""
        if 0 <= index < len(self.grades):
            del self.grades[index]
        else:
            print(f"Invalid index: {index}")

    def report(self):
        """Print a summary report of the student's performance."""
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Grades: {self.grades}")
        print(f"Grades Count: {len(self.grades)}")
        print(f"Passed: {self.is_passed}")
        print(f"Letter Grade: {self.letter}")
        print(f"Honor Roll: {self.honor}")


def start_run():
    """Test run of the Student class."""
    student_a = Student("x001", "Alice")
    student_a.add_grades(100)
    student_a.add_grades("Fifty")  # Invalid grade, ignored
    student_a.calc_average()
    student_a.check_honor()
    student_a.delete_grade(5)  # Invalid index
    student_a.report()


start_run()
