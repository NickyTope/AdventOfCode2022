import unittest
import day13

input = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""

class MyTestCase(unittest.TestCase):
    def test_part1(self):
        result = day13.part1(input)
        self.assertEqual(13, result)

    def test_part2(self):
        result = day13.part2(input)
        self.assertEqual(140, result)


if __name__ == '__main__':
    unittest.main()
