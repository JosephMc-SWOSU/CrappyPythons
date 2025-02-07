class Student:
<<<<<<< HEAD
    def __init__(self, first, last, gpa):
        self.first = first # first name
        self.last = last   # last name
        self.gpa = gpa     # grade point average

    def get_gpa(self):
        return self.gpa

    def get_last(self):
        return self.last

    def to_string(self):
        return self.first + ' ' + self.last + ' (GPA: ' + str(self.gpa) + ')'

class Course:
    def __init__(self):
        self.roster = []  # list of Student objects

    def add_student(self, student):
        self.roster.append(student)

    def get_deans_list(self):
        # Type your code here
        deans_list = []
        for student in self.roster:
            if student.get_gpa() >= 3.5:
                deans_list.append(student)
        deans_list.sort(key=lambda student: student.get_last())
        return deans_list
    

if __name__ == "__main__":
    course = Course()

    course.add_student(Student('Henry', 'Nguyen', 3.5))
    course.add_student(Student('Brenda', 'Stern', 2.0))
    course.add_student(Student('Lynda', 'Robinson', 3.2))
    course.add_student(Student('Sonya', 'King', 3.9))
    course.add_student(Student('Tina', 'Smith', 2.8))
    course.add_student(Student('John', 'Doe', 3.4))
    course.add_student(Student('Jane', 'Doe', 3.2))
    course.add_student(Student('David', 'Smith', 1.6))
    

    deans_list = course.get_deans_list()
    print("Dean's list:")
    for student in deans_list:
        print(student.to_string())
=======
    
    def __init__(self, first_name, last_name, gpa):
        self.first_name = first_name
        self.last_name = last_name
        self.gpa = gpa
    
    def get_gpa(self):
        return self.gpa

class Course:
    
    def __init__(self):
        self.roster = []
    
    def add_student(self, student):
        self.roster.append(student)
    
    def get_deans_list(self):
        deans_list = [student for student in self.roster if student.get_gpa() >= 3.5]
        return deans_list

def main():
    course = Course()
    
    course.add_student(Student("John", "Doe", 3.6))
    course.add_student(Student("Jane", "Smith", 3.4))
    course.add_student(Student("Alice", "Johnson", 3.8))
    course.add_student(Student("Bob", "Brown", 3.2))

    deans_list = course.get_deans_list()
    
    print("Dean's List:")
    for student in deans_list:
        print(f"{student.first_name} {student.last_name} with GPA: {student.get_gpa()}")

if __name__ == "__main__":
    main()
>>>>>>> 9e6b45d9b282c3b0802cfc1f626d91c598ec9169
