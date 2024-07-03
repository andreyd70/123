import unittest
from main import Student

class TestStudent(unittest.TestCase):
    def test_walk_distance(self):
        student = Student('Tim')
        for _ in range(10):
            student.walk()
        self.assertEqual(student.distance, 500, "Дистанции не равны: {} != 500".format(student.distance))

    def test_run_distance(self):
        student = Student('Tom')
        for _ in range(10):
            student.run()
        self.assertEqual(student.distance, 1000, "Дистанции не равны: {} != 1000".format(student.distance))

    def test_compete(self):
        runner = Student('Tim')
        walker = Student('Tom')
        for _ in range(10):
            runner.run()
            walker.walk()
        self.assertGreater(runner.distance, walker.distance, "{} должен преодолеть дистанцию больше, чем {}".format(runner.name, walker.name))

if __name__ == '__main__':
    unittest.main()