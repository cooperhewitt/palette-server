#!/usr/bin/env python

import roygbiv
import webcolors
import json
import Image

def closest_colour(requested_colour):
    min_colours = {}
        
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name

    return min_colours[min(min_colours.keys())]
        
def get_closest(hex):

    rgb = webcolors.hex_to_rgb(hex)
    
    try:
        closest_name = actual_name = webcolors.rgb_to_name(rgb)
    except ValueError:
        closest_name = closest_colour(rgb)
        actual_name = None
        
    if actual_name:
        actual = webcolors.name_to_hex(actual_name)
    else:
        actual = None

    closest = webcolors.name_to_hex(closest_name)
    return actual, closest

def prep(hex):

    web_actual, web_closest = get_closest(hex)
    
    return {
        'colour': hex,
        'closest': web_closest,
    }

def get_colours(path):

    roy = roygbiv.Roygbiv(path)
    average = roy.get_average_hex()
    palette = roy.get_palette_hex()
    
    average = prep(average)
    palette = map(prep, palette)

    return { 'reference-closest': 'css3', 'average': average, 'palette': palette }

if __name__ == '__main__':

    import sys
