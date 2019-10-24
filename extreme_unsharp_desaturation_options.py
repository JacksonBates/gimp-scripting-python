#!/usr/bin/env python

# Tutorial available at: https://www.youtube.com/watch?v=5Ld8Todog5s
# Feedback welcome: jacksonbates@hotmail.com

from gimpfu import *

def extreme_unsharp_desaturation_options(image, drawable, radius, amount, mode):
    pdb.gimp_image_undo_group_start(image)
    threshold = 0
    pdb.plug_in_unsharp_mask(image, drawable, radius, amount, threshold) 
    pdb.gimp_desaturate_full(drawable, mode)
    pdb.gimp_image_undo_group_end(image)
    

register(
    "python-fu-extreme-unsharp-desaturation-options",
    "Unsharp mask and desaurate image, with options",
    "Run an unsharp mask with variables set by user",
    "Jackson Bates", "Jackson Bates", "2015",
    "Extreme unsharp and desaturate options...",
    "RGB",
    [
        (PF_IMAGE, "image", "takes current image", None),
        (PF_DRAWABLE, "drawable", "Input layer", None),
        (PF_SLIDER, "radius", "Radius", 5, (0, 500, 0.5)),
        # note extra tuple (min, max, step)
        (PF_SLIDER, "amount", "Amount", 5.0, (0, 10, 0.1)),
        (PF_RADIO, "mode", "Set Desauration mode: ", DESATURATE_LIGHTNESS,
            (
                 ("Lightness", DESATURATE_LIGHTNESS),
                 ( "Luminosity", DESATURATE_LUMINOSITY),
                 ("Average", DESATURATE_AVERAGE)
            )
         )
    ],
    [],
    extreme_unsharp_desaturation_options, menu="<Image>/Filters/Enhance")

main()
