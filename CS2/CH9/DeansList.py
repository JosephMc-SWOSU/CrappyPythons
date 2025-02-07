class Student:
    
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