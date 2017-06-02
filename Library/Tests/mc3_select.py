#!/usr/local/bin/python3
"""
A subscript of mc3 to select a sample of a catalog based on specified criteria.
"""

from AstroLib import *

################################################################################

def mc3_select( args ):

    ##  Parser.

    Parser  = Io.ArgParser( args )

    Parser.add_argument(
        name            = "configs_file",
        default         = "selection.cfg",
        type            = str,
        key             = None,
        flag            = "-c",
        contains        = None,
        required        = True,
        description     = "The configs file for selection criteria."
    )

    Parser.add_argument(
        name            = "in_file",
        default         = None,
        type            = str,
        key             = None,
        flag            = "-i",
        contains        = None,
        required        = True,
        description     = "The input file to read."
    )

    Parser.add_argument(
        name            = "out_file",
        default         = None,
        type            = str,
        key             = None,
        flag            = "-o",
        contains        = None,
        required        = True,
        description     = "The file to write selected sample to."
    )

    Parser.parse_arguments()
    Parser.check_satisfied()

    configs_file    = Parser.get("configs_file")
    in_file         = Parser.get("in_file")
    out_file        = Parser.get("out_file")

    ##  Reading in.

    print()
    print(
        "Reading input from %s and selection configs from %s."
        % (in_file,configs_file)
    )

    configs         = Io.read( configs_file )
    cat             = Io.read( in_file )

    print( "There were %i lines in %s" %(cat.size,in_file) )

    ##  Perform selection.

    print()
    print( "Performing the following selections:" )

    for i in range( len(configs) ):

        column      = configs["column"][i]
        condition   = configs["condition"][i]
        value       = configs["value"][i]

        print( "%10s    %s %s" % (column,condition,value) )

        if condition == ">":

            cat     = cat[
                np.where( cat[ column ]   > value )[0]
            ]

        elif condition == ">=":

            cat     = cat[
                np.where( cat[ column ]  >= value )[0]
            ]

        elif condition == "<":

            cat     = cat[
                np.where( cat[ column ]   < value )[0]
            ]

        elif condition == "<=":

            cat     = cat[
                np.where( cat[ column ]  <= value )[0]
            ]

        elif condition == "==":

            cat     = cat[
                np.where( cat[ column ]  == value )[0]
            ]

    ##  Write selected sample to out_file.

    print()
    print( "Writing %i lines to %s." % (cat.size,out_file) )

    Io.write( out_file, cat )

    print()
