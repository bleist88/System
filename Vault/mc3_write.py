#!/usr/local/bin/python3
"""
A subscript of mc3 to write output.
"""

from AstroLib import *

################################################################################

def mc3_write( args ):

    Parser  = Io.ArgParser( args )

    Parser.add_argument(
        name            = "out_file",
        default         = None,
        type            = str,
        key             = None,
        flag            = "-o",
        contains        = None,
        required        = True,
        description     = "File the output is written to."
    )

    Parser.add_argument(
        name            = "fits_file",
        default         = None,
        type            = str,
        key             = None,
        flag            = "-f",
        contains        = None,
        required        = True,
        description     = "Configurations file to create an Mc3.Cube()."
    )

    Parser.add_argument(
        name            = "configs_file",
        default         = None,
        type            = str,
        key             = None,
        flag            = "-c",
        contains        = None,
        required        = True,
        description     = "Configurations file to create an Mc3.Cube()."
    )

    Parser.add_argument(
        name            = "select_file",
        default         = None,
        type            = str,
        key             = None,
        flag            = "-s",
        contains        = None,
        required        = False,
        description     = "Configurations file for mc3_select."
    )

    Parser.parse_arguments()
    Parser.check_satisfied()

    if Parser.satisfied:

        out_file        = Parser.get( "out_file" )
        fits_file       = Parser.get( "fits_file" )
        configs_file    = Parser.get( "configs_file" )

        ##  Read in the cfg file and write.

        configs     = Io.read( configs_file )
        Cube        = Mc3.Cube( fits_file )

        Cube.write_specific(
            out_file, configs["extension"], configs["column"], configs["name"]
        )

        ##  Rewrite the file using selection if selection file given.

        select_file  = Parser.get("select_file")

        if select_file is not None:

            args    = [ "-i", out_file, "-o", out_file, "-c", select_file ]

            Mc3.Scripts.mc3_select( args )
