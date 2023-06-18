


class CourseCatalog(object):

    def __init__(self, college = 'CST', department = 'CIS', style = 'LECTURE', type = 'Electives', course_number = -999 ):
        self.course_catalog_id = course_catalog_id
        self.college = college
        self.department department
        self.style = style
        self.type = type
        self.course_number = course_number


    def load_from_db(self):
        '''
        '''
        pass


class Course(object):

    def __init__(self, course_number, CRN, year, semester, instructor_id):
        self.course_number = course_number
        self.CRN = CRN
        self.year = year
        self.semester = semester
        self.instructor_id = instructor_id

    
