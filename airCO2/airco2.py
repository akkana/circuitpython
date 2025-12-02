#!/usr/bin/env python3

# SCD40 CO2 air quality monitor
# driven by an ESP32 Reverse Feather S3.
# 800 ppm is a common suggestion for a level of concern.
# 400ppm is often cited as a typical outside level, but at 6500 feet,
# I'm getting indoor readings at my desk of more like 335-425ppm.

import time

import board
import digitalio

import adafruit_scd4x

from adafruit_max1704x import MAX17048

# Set up the graphical display
import displayio
import terminalio
from adafruit_display_text import label

display = board.DISPLAY

batterymon = MAX17048(board.I2C())

##################################
TEXT_COLOR = 0xFFFFFF

# max threshold: background color
THRESHOLDS = [      400,      500,      600     , 800    , 1000    , 1200 ]
BG_COLORS  = [ 0x000000, 0x600000, 0x900000, 0xa00000, 0xc00000, 0xf00000 ]

# Make the display context
maingroup = displayio.Group()
display.root_group = maingroup

color_bitmap = displayio.Bitmap(display.width, display.height, 1)
color_palette = displayio.Palette(len(BG_COLORS))
for i, color in enumerate(BG_COLORS):
    color_palette[i] = BG_COLORS[i]

bg_bitmap = displayio.Bitmap(display.width, display.height, len(BG_COLORS))
# maingroup.append(bg_bitmap)
maingroup.append(displayio.TileGrid(bg_bitmap, pixel_shader=color_palette))

# Set up two labels, one for CO2 and one for everything else
co2_label = label.Label(terminalio.FONT, text="Waiting...", color=TEXT_COLOR)
                        # background_tight=False)
co2_text_group = displayio.Group(scale=3, x=10, y=25)
co2_text_group.append(co2_label)  # Subgroup for text scaling
maingroup.append(co2_text_group)

other_label = label.Label(terminalio.FONT, text=" \n ", color=TEXT_COLOR)
other_text_group = displayio.Group(scale=2, x=10, y=75)
other_text_group.append(other_label)  # Subgroup for text scaling
maingroup.append(other_text_group)


def get_bg_color(val):
    for i, thresh in enumerate(THRESHOLDS):
        if val < thresh:
            return i
    return i


##################################
# Set up the CO2 sensor
i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
scd4x = adafruit_scd4x.SCD4X(i2c)
# print("Serial number:", [hex(i) for i in scd4x.serial_number])

scd4x.start_periodic_measurement()
print("Waiting for first measurement....")


##################################
# Set up the button(s)
button = digitalio.DigitalInOut(board.BUTTON)
button.switch_to_input(pull=digitalio.Pull.UP)


##################################
# Finally, the main loop

while True:
    if scd4x.data_ready:
        # co2_label.text = "CO2: %d ppm\nTemp: %d°F\nHum: %d%%" % (
        #     scd4x.CO2, int(scd4x.temperature * (212-32)/100) + 32,
        #     scd4x.relative_humidity)
        co2_label.text = "CO2: %d ppm" % (scd4x.CO2)
        if not button.value:
            other_label.text = "\nBattery: %d%%" % int(batterymon.cell_percent)
        else:
            other_label.text = "Temp: %d° F\nHum: %d%%" % (
                int(scd4x.temperature * (212-32)/100) + 32,
                scd4x.relative_humidity)
        # Do something to change the color of bg_tilegrid here
        bgindex = get_bg_color(scd4x.CO2)
        print("Color would be 0x%x" % bgindex)
        # co2_label.background_color = BG_COLORS[bgindex]
        bg_bitmap.fill(bgindex)

        print("CO2: %d ppm" % scd4x.CO2)
        print("Temperature: %0.1f *C" % scd4x.temperature)
        print("Humidity: %0.1f %%" % scd4x.relative_humidity)
        print()
    time.sleep(1)
