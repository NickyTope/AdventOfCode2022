import unittest
import day14

input = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""

class MyTestCase(unittest.TestCase):
    def test_part1(self):
        result = day14.part1(input)
        self.assertEqual(24, result)

    def test_part2(self):
        result = day14.part2(input)
        self.assertEqual(93, result)


if __name__ == '__main__':
    unittest.main()
