Some Tests and Library Routines for the ESP32 Reverse TFT Feather

The ESP32 Reverse TFT Feather isn't very well documented and I found
a lot of things about it confusing, so here are some tests I found
that worked, and a library (rev_tft_feather.py) that might help.

One thing that was confusing was getting CircuitPython onto it in
the first place. The instructions at
https://learn.adafruit.com/esp32-s3-reverse-tft-feather/install-circuitpython
didn't work for me: I copied
adafruit-circuitpython-adafruit_feather_esp32s3_reverse_tft-en_US-10.0.3.uf2
to FTHRS3BOOT, but then nothing happened, the Feather didn't reset and
the CIRCUITPYTHON disk never appeared.
I also tried going to *Open Installer* on
https://circuitpython.org/board/adafruit_feather_esp32s3_reverse_tft/
(using Chromium: Firefox doesn't support serial ports)
and choosing *Full CircuitPython 10.0.3 Install*, which appeared to
install a bootloader but then hung when it got to installing the UF2.
What finally worked was using OpenInstaller to *Install Boatloader Only*
(apparently it hadn't succeeded in installing a new bootloader when I tried
the full install), then going back to the learn.adafruit.com page and
manually installing by copying the UF2.

Your mileage may vary, of course. Good luck! It's a wonderful board
once you get it working.
