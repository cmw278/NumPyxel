from typing import Iterator

import numpy as np

from ..crgb import CRGB
from .display import LEDWindow


class _LEDRef:

    def __init__(self, value: np.ndarray) -> None:
        self._value = value

    def set_crgb(self, colour: CRGB) -> None:
        self._value[:] = colour[:]


class LEDStrip:

    def __init__(
            self,
            length: int,
            window: LEDWindow) -> None:
        self._buffer = np.zeros((length, 3), dtype="uint8")
        self._window = window

    def show(self) -> None:
        self._window.clear()
        for i, pixel in enumerate(self._buffer):
            self._window.set_led(i, pixel)
        self._window.show()

    def __iter__(self) -> Iterator[_LEDRef]:
        for pixel in self._buffer:
            yield _LEDRef(pixel)

    def __getitem__(self, key: int) -> _LEDRef:
        if isinstance(key, int):
            return _LEDRef(self._buffer[key])
        raise NotImplementedError(f"Unknown key '{key}'")

    def __setitem__(self, key: int, value: CRGB) -> None:
        if isinstance(key, int):
            _LEDRef(self._buffer[key]).set_crgb(value)
            return
        raise NotImplementedError(f"Unknown key '{key}'")
