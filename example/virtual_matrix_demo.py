import cv2
import time

from fastled import CRGB, Colours
from fastled.mock import LEDStrip, LEDWindow
from fastled import pixel_map

"""Virtual LED Matrix Demo

The LEDs in out 6x9 matrix start from the bottom-left,
and LEDs are connected as follows:

    53 ← 52 ← 51 ← 50 ← 49 ← 48 ← 47 ← 46 ← 45
                                             ↑
    36 → 37 → 38 → 39 → 40 → 41 → 42 → 43 → 44
    ↑
    35 ← 34 ← 33 ← 32 ← 31 ← 30 ← 29 ← 28 ← 27
                                             ↑
    18 → 19 → 20 → 21 → 22 → 23 → 24 → 25 → 26
    ↑
    17 ← 16 ← 15 ← 14 ← 13 ← 12 ← 11 ← 10 ← 09
                                             ↑
    00 → 01 → 02 → 03 → 04 → 05 → 06 → 07 → 08

We can test our different patterns using a virtual matrix
that is mapped to the same layout.
"""
VIRTUAL_MATRIX_LAYOUT = pixel_map.BottomLeftZigzagRows
HEIGHT = 6
WIDTH = 9

# Change the speed of the demo here.
DELAY = 0.1


def wait(seconds: float) -> None:
    future = time.time() + seconds
    while time.time() < future:
        match cv2.waitKey(1):
            case 27:  # ESC key
                raise SystemExit(0)


def colour_leds_in_physical_order(leds: LEDStrip, colour: CRGB) -> None:
    # We can iterate over the LEDs in the strip. The virtual
    # LEDs should light up in the order our physical LEDs are connected.
    for led in leds:
        led.set_crgb(colour)
        leds.show()
        wait(DELAY)


def colour_leds_in_grid_order(leds: LEDStrip, colour: CRGB) -> None:
    # We can also use the layout to map (x, y) coordinates to LED indices.
    led_map = VIRTUAL_MATRIX_LAYOUT(width=WIDTH, height=HEIGHT)

    # Rows start from the top.
    for y in range(HEIGHT):
        # Columns start from the left.
        for x in range(WIDTH):
            # Get LED index.
            index = led_map.get_index(x, y)

            # Turn LED on.
            leds[index] = colour
            leds.show()
            wait(DELAY)


def run_demo(leds: LEDStrip) -> None:
    # LEDs use 8-bits per colour. FastLED uses uint8_t[3] to represent
    # colour values. CRGB is a convenience class that represents red,
    # green, and blue channel values.
    for colour in Colours:
        colour_leds_in_physical_order(leds, CRGB(colour))

    colour_leds_in_grid_order(leds, CRGB(0xA2D6F9))  # A nice colour.
    colour_leds_in_grid_order(leds, CRGB(0x000000))  # Black.


if __name__ == "__main__":
    # Initialise the virtual LED matrix.
    window = LEDWindow(
        window_title = f"Virtual LED Matrix Demo",
        width=WIDTH,
        height=HEIGHT,
        map_type=VIRTUAL_MATRIX_LAYOUT
    )

    # LEDStrip is representative of how we can interact with
    # FastLED in Arduino, i.e. We can get and set LED colour
    # using the [] operator, while LEDStrip.show() must be
    # called to apply the latest colours.
    leds = LEDStrip(54, window)

    print("Welcome to the Virtual LED Matrix Demo!")
    print("Press [ESC] to exit...")

    while True:
        run_demo(leds)
