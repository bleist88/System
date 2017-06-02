#!/usr/local/bin/python3
"""
Mc3.combine subsript of mc3.
"""

from AstroLib import *

################################################################################

def mc3_combine( args ):

    Parser  = Io.ArgParser( args )

    Parser.add_argument(
        name            = "out_file",
        default         = None,
        type            = str,
        key             = None,
        flag            = "-o",
        contains        = None,
        required        = True,
        description     = "The file the combined catalog is written to."
    )

    Parser.add_argument(
        name            = "configs_file",
        default         = None,
        type            = str,
        key             = None,
        flag            = "-c",
        contains        = None,
        required        = False,
        description     = "Configurations file to create an Mc3.Cube()."
    )

    Parser.parse_arguments()
    Parser.check_satisfied()

    if Parser.satisfied:

        out_file        = Parser.get( "out_file" )
        configs_file    = Parser.get( "configs_file" )

        configs         = Io.read( configs_file )

        ## Run combine on the set of catalogs.

        combined        = Mc3.combine(
            configs["catalogs"], configs["Rc"][0], id_col=configs["id_col"][0],
            x_col=configs["x_col"][0], y_col=configs["y_col"][0]
        )

        Io.write( out_file, combined )
