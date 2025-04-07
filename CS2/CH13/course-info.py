class Course:
    def __init__(self, course_number, course_title):
        self.course_number = course_number
        self.course_title = course_title

    def print_info(self):
        print('Course Information:')
        print(f'   Course Number: {self.course_number}')
        print(f'   Course Title: {self.course_title}')


class OfferedCourse(Course):
    def __init__(self, course_number, course_title, instructor_name, location, class_time):
        super().__init__(course_number, course_title)
        self.instructor_name = instructor_name
        self.location = location
        self.class_time = class_time


if __name__ == "__main__":
    course_number = input("Enter course number: ")
    course_title = input("Enter course title: ")

    o_course_number = input("Enter offered course number: ")
    o_course_title = input("Enter offered course title: ")
    instructor_name = input("Enter instructor name: ")
    location = input("Enter location: ")
    class_time = input("Enter class time: ")

    my_course = Course(course_number, course_title)
    my_course.print_info()

    my_offered_course = OfferedCourse(
        o_course_number, o_course_title, instructor_name, location, class_time
    )
    my_offered_course.print_info()

    print(f'   Instructor Name: {my_offered_course.instructor_name}')
    print(f'   Location: {my_offered_course.location}')
    print(f'   Class Time: {my_offered_course.class_time}')