from unittest import TestCase
from parameterized import parameterized

from fastled.mock.display import Spacing


class TestSpacing(TestCase):

    def setUp(self) -> None:
        self.spacing = Spacing(20)

    @parameterized.expand([
        (0, 0),
        (1, 20),
        (12, 240),
    ])
    def test_left(self, spaces: int, expected: int) -> None:
        actual = self.spacing.left(spaces)
        self.assertEqual(expected, actual,
                         f"The left edge should be {expected}")

    @parameterized.expand([
        (0, 10),
        (1, 30),
        (12, 250),
    ])
    def test_center(self, spaces: int, expected: int) -> None:
        actual = self.spacing.center(spaces)
        self.assertEqual(expected, actual,
                         f"The center should be {expected}")

    @parameterized.expand([
        (0, 20),
        (1, 40),
        (12, 260),
    ])
    def test_right(self, spaces: int, expected: int) -> None:
        actual = self.spacing.right(spaces)
        self.assertEqual(expected, actual,
                         f"The right edge should be {expected}")
