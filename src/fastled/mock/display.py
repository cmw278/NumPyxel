from __future__ import annotations

from typing import Any, Tuple, Type
import cv2
import numpy as np

from .. import pixel_map


class Spacing:

    def __init__(self, distance: int) -> None:
        self._distance = distance + (distance % 2)
        self._center = int(self._distance * 0.5)

    def left(self, spaces: int) -> int:
        return spaces * self._distance

    def right(self, spaces: int) -> int:
        return self.left(spaces + 1)

    def center(self, spaces: int) -> int:
        return self.left(spaces) + self._center


class LEDWindow:

    __INITIALISED = False

    def __new__(cls: type[LEDWindow], *args: Any, **kwargs: Any) -> LEDWindow:
        if not cls.__INITIALISED:
            cv2.startWindowThread()
            cls.__INITIALISED = True
        new_member = object.__new__(cls)
        new_member.__init__(*args, **kwargs)
        return new_member

    def __del__(self) -> None:
        if cv2.getWindowProperty(self._window_title, cv2.WND_PROP_VISIBLE):
            cv2.destroyWindow(self._window_title)

    def __init__(
            self,
            window_title: str,
            width: int = 1,
            height: int = 1,
            led_size: int = 25,
            led_spacing: int = 50,
            map_type: Type[pixel_map.PixelMap]
            = pixel_map.TopLeftProgressiveRows) -> None:
        self._map = map_type(width, height)
        self._window_title = window_title
        self._led_size = int((led_size + (led_size % 2)) * 0.5)
        self._spacing = Spacing(led_spacing)
        self._frame_shape = (
            self._spacing.left(height),
            self._spacing.left(width),
            3
        )
        self._frame = self._blank_frame

        # Create window.
        cv2.namedWindow(self._window_title, cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)
        cv2.resizeWindow(self._window_title, self._frame_shape[1], self._frame_shape[0])

    @property
    def _blank_frame(self) -> np.ndarray:
        return np.full(self._frame_shape, 0x55, dtype="uint8")

    def show(self) -> bool:
        if not cv2.getWindowProperty(self._window_title, cv2.WND_PROP_VISIBLE):
            raise SystemExit(0)
        cv2.imshow(self._window_title, self._frame)

    def clear(self) -> None:
        self._frame = self._blank_frame

    def set_led(self, index: int, pixel_value: np.ndarray) -> None:
        x, y = self._map.get_coordinates(index)
        self._draw_led(x, y, tuple(pixel_value.tolist()))

    def _draw_led(self, x: int, y: int, colour: Tuple[int]) -> None:
        x_pos = self._spacing.center(x)
        y_pos = self._spacing.center(y)
        cv2.circle(
            img=self._frame,
            center=(x_pos, y_pos),
            radius=self._led_size,
            color=colour,
            thickness=cv2.FILLED,
            lineType=cv2.LINE_AA,
        )
