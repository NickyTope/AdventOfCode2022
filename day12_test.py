import unittest
import day12

input_text = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""


class MyTestCase(unittest.TestCase):

    def test_part1(self):
        result = day12.part1(input_text)
        self.assertEqual(31, result)

    def test_part2(self):
        result = day12.part2(input_text)
        self.assertEqual(29, result)

if __name__ == '__main__':
    unittest.main()
