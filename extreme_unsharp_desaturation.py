#!/usr/bin/env python

# Tutorial available at: https://www.youtube.com/watch?v=uSt80abcmJs
# Feedback welcome: jacksonbates@hotmail.com

from gimpfu import *

def extreme_unsharp_desaturation(image, drawable):
    pdb.gimp_image_undo_group_start(image)
    radius = 5.0
    amount = 5.0
    threshold = 0
    pdb.plug_in_unsharp_mask(image, drawable, radius, amount, threshold)
    pdb.gimp_desaturate_full(drawable, DESATURATE_LIGHTNESS)
    pdb.gimp_image_undo_group_end(image)
    

register(
    "python-fu-extreme-unsharp-desaturation",
    "Unsharp mask and desaurate image",
    "Run an unsharp mask with amount set to 5, then desaurate image",
    "Jackson Bates", "Jackson Bates", "2015",
    "Extreme unsharp and desaturate",
    "RGB", 
    [
        (PF_IMAGE, "image", "takes current image", None),
        (PF_DRAWABLE, "drawable", "Input layer", None)
    ],
    [],
    extreme_unsharp_desaturation, menu="<Image>/Filters/Enhance")

main()
