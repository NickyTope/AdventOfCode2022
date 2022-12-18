import unittest
import day15

input = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""

class MyTestCase(unittest.TestCase):
    def test_part1(self):
        t = day15.Sensor(day15.Position(8, 7), day15.Position(2, 10))
        self.assertEqual(9, t.position.distance_to(t.beacon))
        self.assertEqual(True, t.can_see_row(10))
        # for row in range(-2, 18):
        #     print(row, t.empty_in_row(row))
        result = day15.part1(input, 10)
        self.assertEqual(26, result)

    def test_part2(self):
        result = day15.part2(input, 20)
        self.assertEqual(56000011, result)


if __name__ == '__main__':
    unittest.main()
