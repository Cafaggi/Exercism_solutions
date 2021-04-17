class School:
    def __init__(self):
        self.students = list()

    def add_student(self, name, grade):
        if not name or not grade: raise ValueError('There must be name and grade for each student')
        self.students.append((name, grade))

    def roster(self):
        if not self.students: return []
        return [student[0] for student in sorted(self.students, key=lambda x: (x[1],x[0]))]

    def grade(self, grade_number):
        return sorted([student[0] for student in self.students if student[1]==grade_number])
