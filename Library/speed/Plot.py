
from AstroLib import *

################################################################################

##  User Variables.

data_file   = "Speed.dat"
figsize     = 12, 5
bin_range   = 0, 15

##  Read in file and extract Download and Upload Data.

dat     = Io.read( data_file )

##  Figure Set Up.
##  - Speed Vs. Time
##  - Speed Histograme

Fig = pyplot.figure( figsize=figsize )

Ax1 = Fig.add_subplot( 121 )
Ax1.set_xlabel( "Time $[ Hr ]$" )
Ax1.set_ylabel( "Speed $[ Mb/s ]$" )
Ax1.set_xlim( 0, 24 )
Ax1.set_ylim( bin_range[0], bin_range[1] )

Ax2 = Fig.add_subplot( 122 )
Ax2.set_xlabel( "Speed $[ Mb/s ]$" )
Ax2.set_ylabel( "Occurances" )
Ax2.set_xlim( 0, 15 )

##  Plot Data.

time    = dat["hour"] + dat["minute"]/60
d_speed = dat["d_speed"]
u_speed = dat["u_speed"]

Ax1.plot( time, d_speed, "bo", markersize=2, label="Download" )
Ax1.plot( time, u_speed, "go", markersize=2, label="Upload" )

Ax2.hist( dat['d_speed'], 2*bin_range[1], range=bin_range, histtype="step", label="Download" )
Ax2.hist( dat['u_speed'], 2*bin_range[1], range=bin_range, histtype="step", label="Upload" )

Ax1.legend()
Ax2.legend()

Fig.tight_layout()
Fig.savefig("LastSpeed.png")
