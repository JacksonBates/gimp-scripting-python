#!/usr/bin/env python

# Tutorial available at: https://www.youtube.com/watch?v=oNn9D_8d4zQ
# Feedback welcome: jacksonbates@hotmail.com

from gimpfu import *


def lomo_opt(image, drawable, direction):
    pdb.gimp_image_undo_group_start(image)

    #adjust curves on RG and B channels
    s_curve = (0, 0, 96, 64, 128, 128, 160, 192, 255, 255)
    inverted_s_curve = (0, 0, 64, 96, 128, 128, 192, 160, 255, 255)
    num_points = 10
    pdb.gimp_curves_spline(drawable, HISTOGRAM_RED, num_points, s_curve)
    pdb.gimp_curves_spline(drawable, HISTOGRAM_GREEN, num_points, s_curve)
    pdb.gimp_curves_spline(drawable, HISTOGRAM_BLUE, num_points,
                           inverted_s_curve)

    #add new layer & Set to 'overlay'
    opacity_100 = 100
    layer = pdb.gimp_layer_new(image, image.width, image.height, RGB_IMAGE,
                               "Overlay", opacity_100, OVERLAY_MODE)
    layer_position = 0
    pdb.gimp_image_insert_layer(image, layer, None, layer_position)
    
    # blend argument variables
    blend_mode = 0
    paint_mode = 0
    gradient_type = 0
    offset = 0
    repeat = 0
    reverse = False
    supersample = False
    max_depth = 1
    threshold = 0
    dither = True
    
    # arguments for blend, including directions
    # backslash character is used to allow short line lengths
    n = layer, blend_mode, paint_mode, gradient_type, opacity_100, offset, \
        repeat, reverse, supersample,  max_depth, threshold,  dither, \
        layer.width / 2, 0, layer.width / 2, layer.height / 2
    
    ne = layer, blend_mode, paint_mode, gradient_type, opacity_100, offset, \
         repeat, reverse, supersample,  max_depth, threshold,  dither, \
         layer.width, 0, layer.width / 2, layer.height / 2
    
    e = layer, blend_mode, paint_mode, gradient_type, opacity_100, offset, \
        repeat, reverse, supersample,  max_depth, threshold,  dither, \
        layer.width, layer.height / 2, layer.width / 2, layer.height / 2
    
    se = layer, blend_mode, paint_mode, gradient_type, opacity_100, offset, \
         repeat, reverse, supersample,  max_depth, threshold,  dither, \
         layer.width, layer.height, layer.width / 2, layer.height / 2
    
    s = layer, blend_mode, paint_mode, gradient_type, opacity_100, offset, \
        repeat, reverse, supersample,  max_depth, threshold,  dither, \
        layer.width / 2, layer.height, layer.width / 2, layer.height / 2
    
    sw = layer, blend_mode, paint_mode, gradient_type, opacity_100, offset, \
         repeat, reverse, supersample,  max_depth, threshold,  dither, \
         0, layer.height, layer.width / 2, layer.height / 2
    
    w = layer, blend_mode, paint_mode, gradient_type, opacity_100, offset, \
        repeat, reverse, supersample,  max_depth, threshold,  dither, \
        0, layer.height / 2, layer.width / 2, layer.height / 2
    
    nw = layer, blend_mode, paint_mode, gradient_type, opacity_100, offset, \
         repeat, reverse, supersample,  max_depth, threshold,  dither, \
         0, 0, layer.width / 2, layer.height / 2
    
    # blend tool, linear gradient (to add user entry,
    # based on diagonal desired for gradient direction?)
    # the number used denotes the list position of the direction chosen
    if direction == 0:
        pdb.gimp_edit_blend(*n)
    elif direction == 1:
        pdb.gimp_edit_blend(*ne)
    elif direction == 2:
        pdb.gimp_edit_blend(*e)
    elif direction == 3:
        pdb.gimp_edit_blend(*se)
    elif direction == 4:
        pdb.gimp_edit_blend(*s)
    elif direction == 5:
        pdb.gimp_edit_blend(*sw)
    elif direction == 6:
        pdb.gimp_edit_blend(*w)
    else:
        pdb.gimp_edit_blend(*nw)
        
    #merge all layers, and end undo group
    layer = pdb.gimp_image_merge_visible_layers(image, 0)
    pdb.gimp_image_undo_group_end(image)
    

register(
    "python-fu-lomo-opt",
    "Lomo effect opt",
    "Creates a lomo effect on a given image and user input",
    "Jackson Bates", "Jackson Bates", "2015",
    "Lomo opt...",
    "RGB", # type of image it works on (*, RGB, RGB*, RGBA etc...)
    [
        (PF_IMAGE, "image", "takes current image", None),
        (PF_DRAWABLE, "drawable", "Input layer", None),
        (PF_OPTION, "direction", "Direction: ", 0,
             (
                 ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
              )
         )
    ],
    [],
    lomo_opt, menu="<Image>/Filters")  # second item is menu location

main()
