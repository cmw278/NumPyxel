from typing import Tuple, Type
from unittest import TestCase
from parameterized import parameterized_class

from fastled import pixel_map


def _get_class_name(cls: Type, num: int, params: dict) -> str:
    subject_name = params["map_type"].__name__
    return f"{cls.__name__}_{num:02}_{subject_name}"


@parameterized_class([
    # TopLeftProgressiveRows
    {
        "map_type": pixel_map.TopLeftProgressiveRows,
        "expected_index": 0,
        "expected_coordinates": (0, 0)
    },
    {
        "map_type": pixel_map.TopLeftProgressiveRows,
        "expected_index": 4,
        "expected_coordinates": (0, 1)
    },

    # TopLeftProgressiveColumns
    {
        "map_type": pixel_map.TopLeftProgressiveColumns,
        "expected_index": 0,
        "expected_coordinates": (0, 0)
    },
    {
        "map_type": pixel_map.TopLeftProgressiveColumns,
        "expected_index": 4,
        "expected_coordinates": (1, 0)
    },

    # TopRightProgressiveRows
    {
        "map_type": pixel_map.TopRightProgressiveRows,
        "expected_index": 0,
        "expected_coordinates": (3, 0)
    },
    {
        "map_type": pixel_map.TopRightProgressiveRows,
        "expected_index": 4,
        "expected_coordinates": (3, 1)
    },

    # TopRightProgressiveColumns
    {
        "map_type": pixel_map.TopRightProgressiveColumns,
        "expected_index": 0,
        "expected_coordinates": (3, 0)
    },
    {
        "map_type": pixel_map.TopRightProgressiveColumns,
        "expected_index": 4,
        "expected_coordinates": (2, 0)
    },

    # TopLeftZigzagRows
    {
        "map_type": pixel_map.TopLeftZigzagRows,
        "expected_index": 0,
        "expected_coordinates": (0, 0)
    },
    {
        "map_type": pixel_map.TopLeftZigzagRows,
        "expected_index": 4,
        "expected_coordinates": (3, 1)
    },

    # TopLeftZigzagColumns
    {
        "map_type": pixel_map.TopLeftZigzagColumns,
        "expected_index": 0,
        "expected_coordinates": (0, 0)
    },
    {
        "map_type": pixel_map.TopLeftZigzagColumns,
        "expected_index": 4,
        "expected_coordinates": (1, 3)
    },

    # TopRightZigzagRows
    {
        "map_type": pixel_map.TopRightZigzagRows,
        "expected_index": 0,
        "expected_coordinates": (3, 0)
    },
    {
        "map_type": pixel_map.TopRightZigzagRows,
        "expected_index": 4,
        "expected_coordinates": (0, 1)
    },

    # TopRightZigzagColumns
    {
        "map_type": pixel_map.TopRightZigzagColumns,
        "expected_index": 0,
        "expected_coordinates": (3, 0)
    },
    {
        "map_type": pixel_map.TopRightZigzagColumns,
        "expected_index": 4,
        "expected_coordinates": (2, 3)
    },

    # BottomLeftProgressiveRows
    {
        "map_type": pixel_map.BottomLeftProgressiveRows,
        "expected_index": 0,
        "expected_coordinates": (0, 3)
    },
    {
        "map_type": pixel_map.BottomLeftProgressiveRows,
        "expected_index": 4,
        "expected_coordinates": (0, 2)
    },

    # BottomLeftProgressiveColumns
    {
        "map_type": pixel_map.BottomLeftProgressiveColumns,
        "expected_index": 0,
        "expected_coordinates": (0, 3)
    },
    {
        "map_type": pixel_map.BottomLeftProgressiveColumns,
        "expected_index": 4,
        "expected_coordinates": (1, 3)
    },

    # BottomRightProgressiveRows
    {
        "map_type": pixel_map.BottomRightProgressiveRows,
        "expected_index": 0,
        "expected_coordinates": (3, 3)
    },
    {
        "map_type": pixel_map.BottomRightProgressiveRows,
        "expected_index": 4,
        "expected_coordinates": (3, 2)
    },

    # BottomRightProgressiveColumns
    {
        "map_type": pixel_map.BottomRightProgressiveColumns,
        "expected_index": 0,
        "expected_coordinates": (3, 3)
    },
    {
        "map_type": pixel_map.BottomRightProgressiveColumns,
        "expected_index": 4,
        "expected_coordinates": (2, 3)
    },

    # BottomLeftZigzagRows
    {
        "map_type": pixel_map.BottomLeftZigzagRows,
        "expected_index": 0,
        "expected_coordinates": (0, 3)
    },
    {
        "map_type": pixel_map.BottomLeftZigzagRows,
        "expected_index": 4,
        "expected_coordinates": (3, 2)
    },

    # BottomLeftZigzagColumns
    {
        "map_type": pixel_map.BottomLeftZigzagColumns,
        "expected_index": 0,
        "expected_coordinates": (0, 3)
    },
    {
        "map_type": pixel_map.BottomLeftZigzagColumns,
        "expected_index": 4,
        "expected_coordinates": (1, 0)
    },

    # BottomRightZigzagRows
    {
        "map_type": pixel_map.BottomRightZigzagRows,
        "expected_index": 0,
        "expected_coordinates": (3, 3)
    },
    {
        "map_type": pixel_map.BottomRightZigzagRows,
        "expected_index": 4,
        "expected_coordinates": (0, 2)
    },

    # BottomRightZigzagColumns
    {
        "map_type": pixel_map.BottomRightZigzagColumns,
        "expected_index": 0,
        "expected_coordinates": (3, 3)
    },
    {
        "map_type": pixel_map.BottomRightZigzagColumns,
        "expected_index": 4,
        "expected_coordinates": (2, 0)
    },
], class_name_func=_get_class_name )
class TestPixelMap(TestCase):
    map_type: Type[pixel_map.PixelMap]
    expected_index: int
    expected_coordinates: Tuple[int, int]

    def setUp(self) -> None:
        self._map = self.map_type(4, 4)

    def test_get_coordinates(self) -> None:
        expected = self.expected_coordinates
        actual = self._map.get_coordinates(self.expected_index)
        self.assertEqual(expected, actual, f"Coordinates should match {expected}")

    def test_get_index(self) -> None:
        expected = self.expected_index
        actual = self._map.get_index(*self.expected_coordinates)
        self.assertEqual(expected, actual, f"Index should match {expected}")
