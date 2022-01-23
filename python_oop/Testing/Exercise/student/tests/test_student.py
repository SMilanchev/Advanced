from Testing.Exercise.student.project.student import Student
import unittest


class StudentTest(unittest.TestCase):
    def setUp(self):
        self.student = Student('Ivan')

    def test_student_with_none_courses_is_properly_initialized(self):
        self.assertEqual(self.student.name, 'Ivan')
        self.assertEqual(self.student.courses, {})

    def test_student_with_non_none_courses_is_properly_initialized(self):
        self.student = Student('Ivan', 'petko')
        self.assertEqual(self.student.courses, 'petko')

    def test_enroll_add_course(self):
        self.assertEqual(self.student.enroll('Course1', 'notes1'), "Course and course notes have been added.")

    # def test_enroll_when_course_already_added(self):
    #     self.student.enroll('Programming', )

if __name__ == '__main__':
    unittest.main()