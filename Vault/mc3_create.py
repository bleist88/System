#!/usr/local/bin/python3
"""
Mc3.Create subsript of mc3.
"""

from AstroLib import *

################################################################################

def mc3_create( args ):

    Parser  = Io.ArgParser( args )

    Parser.add_argument(
        name            = "fits_file",
        default         = None,
        type            = str,
        key             = None,
        flag            = "-o",
        contains        = None,
        required        = True,
        description     = "File name for fits cube to create."
    )

    Parser.add_argument(
        name            = "configs_file",
        default         = "mc3.cfg",
        type            = str,
        key             = None,
        flag            = "-c",
        contains        = None,
        required        = True,
        description     = "Configurations file to create an Mc3.Cube()."
    )

    Parser.add_argument(
        name            = "images_file",
        default         = "mc3_images.cfg",
        type            = str,
        key             = None,
        flag            = "-i",
        contains        = None,
        required        = True,
        description     = "Image configurations file to create an Mc3.Cube()."
    )

    Parser.parse_arguments()
    Parser.check_satisfied()

    if Parser.satisfied:

        fits_file       = Parser.get( "fits_file" )
        configs_file    = Parser.get( "configs_file" )
        images_file     = Parser.get( "images_file" )

        Mc3.create(
            fits_file, configs_file=configs_file, images_file=images_file
        )
