# airCO2

A CO2 air quality monitor using a SCD-40 sensor,
driven by an ESP32 Reverse Feather S3.

## Required libraries

- adafruit_scd4x (the CO2 sensor)
- adafruit_display_text (for the display)
- adafruit_pixelbuf (for the display)
- adafruit_bitmap_font (for the display)
- adafruit_max1704x.mpy (for battery status)

I think everything else is built in to CircuitPython.

## Wiring

The ESP32 Feather and the SCD-40 both have Stemma QT
connectors, plus a battery with a JST plug (with the same polarity
Adafruit uses for their batteries!)
