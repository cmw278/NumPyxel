from __future__ import annotations

from enum import IntEnum
from typing import Iterator, List, Union


class CRGB:

    def __init__(self, value: int = 0x0) -> None:
        self._value = value

    @property
    def red(self) -> int:
        return (self._value >> 16) & 0xff

    @red.setter
    def red(self, new_value: int) -> None:
        self._value &= 0x00_ff_ff
        self._value |= 0xff_00_00 & (new_value << 16)

    @property
    def green(self) -> int:
        return (self._value >> 8) & 0xff

    @green.setter
    def green(self, new_value: int) -> None:
        self._value &= 0xff_00_ff
        self._value |= 0x00_ff_00 & (new_value << 8)

    @property
    def blue(self) -> int:
        return self._value & 0xff

    @blue.setter
    def blue(self, new_value: int) -> None:
        self._value &= 0xff_ff_00
        self._value |= 0x00_00_ff & new_value

    def __repr__(self) -> str:
        return f"CRGB(value={self._value:#06x})"

    def __iter__(self) -> Iterator[int]:
        yield self.blue
        yield self.green
        yield self.red

    def __getitem__(self, key: Union[int, slice]) -> Union[int, List[int]]:
        return [*self][key]


class Colours(IntEnum):
    RED =       0xFF_00_00
    GREEN =     0x00_FF_00
    BLUE =      0x00_00_FF
    WHITE =     0xFF_FF_FF
    BLACK =     0x00_00_00
