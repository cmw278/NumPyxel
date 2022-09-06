from abc import ABC, abstractmethod

from typing import Tuple


class PixelMap(ABC):

    def __init__(self, width: int, height: int) -> None:
        self._width = width
        self._height = height

    @property
    def _imax(self) -> int:
        return (self._width * self._height) - 1

    @property
    def _wmax(self) -> int:
        return self._width - 1

    @property
    def _hmax(self) -> int:
        return self._height - 1

    @abstractmethod
    def get_coordinates(self, i: int) -> Tuple[int, int]:
        raise NotImplementedError(
            f"{self.__class__.__name__}.get_coordinates() is not implemented."
        )

    @abstractmethod
    def get_index(self, x : int, y: int) -> int:
        raise NotImplementedError(
            f"{self.__class__.__name__}.get_index() is not implemented."
        )


class TopLeftProgressiveRows(PixelMap):
    """
    o → o
      ↙
    o → o
    """
    def get_coordinates(self, i: int) -> Tuple[int, int]:
        x = i % self._width
        y = i // self._width
        return x, y

    def get_index(self, x: int, y: int) -> int:
        return (y * self._width) + x


class TopLeftProgressiveColumns(PixelMap):
    """
    o   o
    ↓ ↗ ↓
    o   o
    """
    def get_coordinates(self, i: int) -> Tuple[int, int]:
        x = i // self._height
        y = i % self._height
        return x, y

    def get_index(self, x: int, y: int) -> int:
        return (x * self._height) + y


class TopRightProgressiveRows(PixelMap):
    """
    o ← o
      ↘
    o ← o
    """
    def get_coordinates(self, i: int) -> Tuple[int, int]:
        x = self._wmax - (i % self._width)
        y = i // self._width
        return x, y

    def get_index(self, x: int, y: int) -> int:
        return (y * self._width) + (self._wmax - x)


class TopRightProgressiveColumns(PixelMap):
    """
    o   o
    ↓ ↖ ↓
    o   o
    """
    def get_coordinates(self, i: int) -> Tuple[int, int]:
        x = self._wmax - (i // self._height)
        y = i % self._height
        return x, y

    def get_index(self, x: int, y: int) -> int:
        return ((self._wmax - x) * self._height) + y


class TopLeftZigzagRows(PixelMap):
    """
    o → o
        ↓
    o ← o
    """
    def get_coordinates(self, i: int) -> Tuple[int, int]:
        x = i % self._width
        y = i // self._width
        if y % 2:
            x = self._wmax - x
        return x, y

    def get_index(self, x: int, y: int) -> int:
        x_comp = self._wmax - x if y % 2 else x
        y_comp = y * self._width
        return x_comp + y_comp


class TopLeftZigzagColumns(PixelMap):
    """
    o   o
    ↓   ↑
    o → o
    """
    def get_coordinates(self, i: int) -> Tuple[int, int]:
        x = i // self._height
        y = i % self._height
        if x % 2:
            y = self._hmax - y
        return x, y

    def get_index(self, x: int, y: int) -> int:
        x_comp = x * self._height
        y_comp = self._hmax - y if x % 2 else y
        return x_comp + y_comp


class TopRightZigzagRows(PixelMap):
    """
    o ← o
    ↓
    o → o
    """
    def get_coordinates(self, i: int) -> Tuple[int, int]:
        x = i % self._width
        y = i // self._width
        if not y % 2:
            x = self._wmax - x
        return x, y

    def get_index(self, x: int, y: int) -> int:
        x_comp = x if y % 2 else self._wmax - x
        y_comp = y * self._width
        return x_comp + y_comp


class TopRightZigzagColumns(PixelMap):
    """
    o   o
    ↑   ↓
    o ← o
    """
    def get_coordinates(self, i: int) -> Tuple[int, int]:
        x = self._wmax - (i // self._height)
        y = i % self._height
        bottom_up = (not x % 2) if self._wmax % 2 else (x % 2)
        if bottom_up:
            y = self._hmax - y
        return x, y

    def get_index(self, x: int, y: int) -> int:
        x_comp = (self._wmax - x) * self._height
        bottom_up = (x % 2) if self._wmax % 2 else (not x % 2)
        y_comp = y if bottom_up else self._hmax - y
        return x_comp + y_comp


class BottomLeftProgressiveRows(PixelMap):
    """
    o → o
      ↖
    o → o
    """
    def get_coordinates(self, i: int) -> Tuple[int, int]:
        x = i % self._width
        y = self._hmax - (i // self._width)
        return x, y

    def get_index(self, x: int, y: int) -> int:
        return self._imax - (y * self._width) + x - self._wmax


class BottomLeftProgressiveColumns(PixelMap):
    """
    o   o
    ↑ ↘ ↑
    o   o
    """
    def get_coordinates(self, i: int) -> Tuple[int, int]:
        x = i // self._height
        y = self._hmax - (i % self._height)
        return x, y

    def get_index(self, x: int, y: int) -> int:
        return (x * self._height) + self._hmax - y


class BottomRightProgressiveRows(PixelMap):
    """
    o ← o
      ↗
    o ← o
    """
    def get_coordinates(self, i: int) -> Tuple[int, int]:
        x = self._wmax - (i % self._width)
        y = self._hmax - (i // self._width)
        return x, y

    def get_index(self, x: int, y: int) -> int:
        return self._imax - ((x % self._width) + (y * self._width))


class BottomRightProgressiveColumns(PixelMap):
    """
    o   o
    ↑ ↙ ↑
    o   o
    """
    def get_coordinates(self, i: int) -> Tuple[int, int]:
        x = self._wmax - (i // self._height)
        y = self._hmax - (i % self._height)
        return x, y

    def get_index(self, x: int, y: int) -> int:
        return self._imax - (x * self._height) - y


class BottomLeftZigzagRows(PixelMap):
    """
    o ← o
        ↑
    o → o
    """
    def get_coordinates(self, i: int) -> Tuple[int, int]:
        x = i % self._width
        y = self._hmax - (i // self._width)
        right_to_left = (not y % 2) if self._hmax % 2 else (y % 2)
        if right_to_left:
            x = self._wmax - x
        return x, y

    def get_index(self, x: int, y: int) -> int:
        right_to_left = (y % 2) if self._hmax % 2 else (not y % 2)
        x_comp = x if right_to_left else self._wmax - x
        y_comp = (self._hmax - y) * self._width
        return x_comp + y_comp


class BottomLeftZigzagColumns(PixelMap):
    """
    o → o
    ↑   ↓
    o   o
    """
    def get_coordinates(self, i: int) -> Tuple[int, int]:
        x = i // self._height
        y = i % self._height
        if not x % 2:
            y = self._hmax - y
        return x, y

    def get_index(self, x: int, y: int) -> int:
        x_comp = x * self._height
        y_comp = y if x % 2 else self._hmax - y
        return x_comp + y_comp


class BottomRightZigzagRows(PixelMap):
    """
    o → o
    ↑
    o ← o
    """
    def get_coordinates(self, i: int) -> Tuple[int, int]:
        x = i % self._width
        y = self._hmax - (i // self._width)
        right_to_left = (y % 2) if self._hmax % 2 else (not y % 2)
        if right_to_left:
            x = self._wmax - x
        return x, y

    def get_index(self, x: int, y: int) -> int:
        x_comp = self._wmax - x if y % 2 else x
        y_comp = (self._hmax - y) * self._width
        return x_comp + y_comp


class BottomRightZigzagColumns(PixelMap):
    """
    o ← o
    ↓   ↑
    o   o
    """
    def get_coordinates(self, i: int) -> Tuple[int, int]:
        x = self._wmax - (i // self._height)
        y = i % self._height
        top_down = (x % 2) if self._wmax % 2 else (not x % 2)
        if top_down:
            y = self._hmax - y
        return x, y

    def get_index(self, x: int, y: int) -> int:
        x_comp = (self._wmax - x) * self._height
        top_down = (x % 2) if self._wmax % 2 else (not x % 2)
        y_comp = self._hmax - y if top_down else y
        return x_comp + y_comp
