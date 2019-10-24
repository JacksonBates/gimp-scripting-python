#!/usr/bin/env python

# GIMP UI examples of options
# Feedback welcome: jacksonbates@hotmail.com

from gimpfu import *

def ui_examples_2(radio_var, option_var, spinner_var, slider_var,
                  adjustment_var, file_var, dirname_var, font_var,
                  brush_var, pattern_var, gradient_var, palette_var):
    return

register(
    "python_fu_ui_examples_2",
    "Show other half of the UI options",
    "Dummy UI 2",
    "Jackson Bates",
    "Jackson Bates",
    "2015",
    "Show more UI Options...",
    "",      # Image type
    [
        (PF_RADIO, "radio_var", "radio", "radio1_value",
            (
                ("radio1_label", "radio1_value"),
                ("radio2_label", "radio2_value")
            )
         ),
        (PF_OPTION, "option_var", "option", 0,
            ("Opt1", "Opt2", "Opt3", "Opt4")
         ),
        (PF_SPINNER, "spinner_var", "spinner", 10, (1, 10, 0.5)),
        (PF_SLIDER, "slider_var",  "slider", 100, (0, 100, 1)),
        (PF_ADJUSTMENT, "adjustment_var", "adjustment", 10, (1, 10, 1)),
        (PF_FILE, "file_var", "file", ""),
        (PF_DIRNAME, "dirname_var", "dirname", "/tmp"),
        (PF_FONT, "font_var", "font", "Sans"),
        (PF_BRUSH, "brush_var", "brush", None),
        (PF_PATTERN, "pattern_var", "pattern", None),
        (PF_GRADIENT, "gradient_var", "gradient", None),
        (PF_PALETTE, "palette_var",  "palette", ""),
    ],
    [],
    ui_examples_2, menu="<Image>/Filters/Languages/Python-Fu" )

main()
