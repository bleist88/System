"""
This script uses the speedtest-cli script to test for internet speed.  This willcontinue to run the script from the command line, write the output to a file.  Read and parse the file.
"""

from AstroLib import *

################################################################################

##  User Variables.

temp_file       = "Speed.out"
data_file       = "Speed.dat"
iterations      = 1000
sleep_time      = 300           ## seconds

##  Run the Speed Test to an output file.
##  Read output file and find "Donwload:" and "Upload:".
##  Record to a ".dat" file along with time.

print( "Running 'speedtest-cli'." )

out     = open( data_file, 'w' )
out.write( "#<  hour        int32\n" )
out.write( "#<  minute      int32\n" )
out.write( "#<  d_speed     float32\n" )
out.write( "#<  u_speed     float32\n" )
out.close()

for i in range( iterations ):

    print( "    Iteration %i." %i )

    ##  Run.

    os.system( "speedtest-cli >> %s" % temp_file )
    time.sleep( sleep_time )

    ##  Variables.

    localtime   = time.localtime()
    hour        = localtime.tm_hour
    minute      = localtime.tm_min
    d_speed     = None
    u_speed     = None

    ##  Read in the output file.

    temp    = Io.get_body( temp_file )

    for i in range( len(temp) ):

        for j in range( len(temp[i]) ):

            if temp[i][j] == "Download:":

                try:
                    d_speed = float( temp[i][j+1] )
                except:
                    continue

            elif temp[i][j] == "Upload:":

                try:
                    u_speed = float( temp[i][j+1] )
                except:
                    continue

    ##  Write to data_file.

    out     = open( data_file, 'a' )

    out.write(
        "    %5i %5i %6.2f %6.2f\n" % (hour, minute, d_speed, u_speed)
    )

    out.close()

    os.system( "rm %s" % temp_file )

##  End.

print( "The speed test has ended." )
