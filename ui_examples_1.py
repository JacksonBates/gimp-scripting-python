#!/usr/bin/env python

# GIMP UI examples of options
# Feedback welcome: jacksonbates@hotmail.com

from gimpfu import *

def ui_examples_1(int_var, float_var, string_var, value_var, color_var,
               colour_var, image_var, layer_var, channel_var, drawable_var,
               toggle_var, boolean_var):
    return

register(
    "python_fu_ui_examples_1",
    "Show half of the UI options",
    "Dummy UI",
    "Jackson Bates",
    "Jackson Bates",
    "2015",
    "Show UI Options...",
    "",      # Image type
    [
        (PF_INT, "int_var", "int", 50),
        (PF_FLOAT, "float_var", "float", 3.14159),
        # I don't know the diference between these PF_INT8, PF_INT16, PF_INT32
        # Assuming bitsize, but I'd love to be further enlightened!
        (PF_STRING, "string_var", "string", "Awesomesauce!"),
        (PF_VALUE, "value_var", "value", "Is this the same as above?!"),
        (PF_TEXT, "text_var", "text", "This accepts a longer string of text"),
        (PF_COLOR, "color_var", "color", (1.0, 1.0, 1.0)),
        (PF_COLOUR, "colour_var", "colour UK sp. :)",(255.0, 255.0, 255.0)),
        (PF_IMAGE, "image_var", "image", None),
        (PF_LAYER, "layer_var", "layer", None),
        (PF_CHANNEL, "channel_var", "channel", None),
        (PF_DRAWABLE, "drawable_var", "drawable", None),
        (PF_TOGGLE, "toggle_var", "toggle", 1),
        (PF_BOOL,   "boolean_var", "Boolean", True),
    ],
    [],
    ui_examples_1, menu="<Image>/Filters/Languages/Python-Fu" )

main()
