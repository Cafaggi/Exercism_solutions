
class Garden:

    def __init__(self, diagram, students = []):

        self.plant_map = {  'G': 'Grass', 
                            'C': 'Clover', 
                            'R':'Radishes', 
                            'V':'Violets'}

        default_students = ['Alice',
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

        self.students = students if students else default_students
        self.students.sort()

        self.diagram = diagram.split("\n")

    
    def plants(self, student):
        index_end = (self.students.index(student)+1)*2
        plant_list = self.diagram[0][index_end-2:index_end]+self.diagram[1][index_end-2:index_end]
        return [self.plant_map[plant] for plant in plant_list]
