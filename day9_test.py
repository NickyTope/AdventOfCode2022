import unittest
import day9


class MyTestCase(unittest.TestCase):


    def test_part1(self):
        in_text = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""
        result = day9.part1(in_text)
        self.assertEqual(13, result)

    def test_part12self(self):
        in_text = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
"""
        result = day9.part2(in_text)
        self.assertEqual(36, result)


if __name__ == '__main__':
    unittest.main()
