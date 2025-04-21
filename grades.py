# grades.py

class GradeCalculator:
    def __init__(self, grades):
        self.grades = grades

    def calculate_weighted_average(self, weights):
        """Calculate weighted average based on given weights."""
        total_weight = sum(weights)
        weighted_sum = sum(grade * weight for grade, weight in zip(self.grades, weights))
        return weighted_sum / total_weight if total_weight != 0 else 0

    def drop_lowest_grade(self):
        """Remove the lowest grade from the list."""
        if len(self.grades) > 1:
            self.grades.remove(min(self.grades))
        return self.grades

    def apply_extra_credit(self, extra):
        """Add extra credit to each grade."""
        self.grades = [min(grade + extra, 100) for grade in self.grades]
        return self.grades

    def convert_to_letter(self, average):
        """Convert numeric grade to letter grade."""
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

    def compute_final_grade(self, use_weights=False, weights=None):
        """Compute the final grade with optional weighting."""
        if use_weights and weights:
            return self.calculate_weighted_average(weights)
        return sum(self.grades) / len(self.grades) if self.grades else 0
