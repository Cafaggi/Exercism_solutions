DEFAULT_STUDENTS = ['Alice',
                    'Bob',
                    'Charlie',
                    'David',
                    'Eve',
                    'Fred',
                    'Ginny',
                    'Harriet',
                    'Ileana',
                    'Joseph',
                    'Kincaid',
                    'Larry']

PLANT_MAP = {'G': 'Grass', 
            'C': 'Clover', 
            'R':'Radishes', 
            'V':'Violets'}


class Garden:

    def __init__(self, diagram, students = DEFAULT_STUDENTS):

        self.students = students
        self.diagram = diagram.splitlines()
        self.students_garden = self.create_students_map()
    
    def plants(self, student):
        return self.students_garden[student]

    def create_students_map(self):

        '''
        Create a dictionary with all de students as keys and its garden's plants as values
        '''

        student_map = dict()
        self.students.sort()

        for student in self.students:
            index_end = (self.students.index(student)+1)*2
            plant_list = self.diagram[0][index_end-2:index_end]+self.diagram[1][index_end-2:index_end]
            student_map[student] = [PLANT_MAP[plant] for plant in plant_list]

        return student_map
        
