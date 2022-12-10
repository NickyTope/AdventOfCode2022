import unittest
import day8

class MyTestCase(unittest.TestCase):


    def test_part1(self):
        in_text = """30373
25512
65332
33549
35390
"""
        result = day8.part1(in_text)
        self.assertEqual(21, result)


    def test_part2(self):
        in_text = """30373
25512
65332
33549
35390
"""
        result = day8.part2(in_text)
        self.assertEqual(8, result)

if __name__ == '__main__':
    unittest.main()
