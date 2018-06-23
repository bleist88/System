#!/usr/local/bin/python3
"""
Mc3.add subsript of mc3.
"""

from AstroLib import *

################################################################################

def mc3_add( args ):

    Parser  = Io.ArgParser( args )

    Parser.add_argument(
        name            = "fits_file",
        default         = None,
        type            = str,
        key             = None,
        flag            = "-f",
        contains        = None,
        required        = True,
        description     = "The existing FITS Cube to add a catalog."
    )

    Parser.add_argument(
        name            = "configs_file",
        default         = None,
        type            = str,
        key             = None,
        flag            = "-c",
        contains        = None,
        required        = True,
        description     = "Configurations file with info to add to the Cube."
    )

    Parser.add_argument(
        name            = "addition",
        default         = None,
        type            = str,
        key             = None,
        flag            = "-a",
        contains        = None,
        required        = True,
        description     = "Name of the extension in configs_file to add."
    )

    Parser.parse_arguments()
    Parser.check_satisfied()

    if Parser.satisfied:

        fits_file       = Parser.get( "fits_file" )
        configs_file    = Parser.get( "configs_file" )
        addition        = Parser.get( "addition" )

        Mc3.add( fits_file, addition, configs_file=configs_file )
