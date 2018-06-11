
from __imports__ import *

################################################################################

print()
print( "Simple Ehrenfest Model:" )

##  ========================================================================  ##
##  User Variables

Na          = 30        ##  Number of initial particles in A.
Nb          = 0          ##  Number of initial particles in B.
R_min       = 10         ##  Minimum number of particles to swap per dt.
R_max       = Na         ##  Maximum number of particles to swap per dt.
net_time    = 1e8       ##  Total number of time steps.

marker      = "bx"
ms          = 1

show        = True
write       = False

sm_std      = 15

##  ========================================================================  ##
##  Basic Setup

##  Calculate internal variables.

N       = Na + Nb
Time    = np.arange( 0, net_time, 1, dtype="int32" )
balance = np.zeros( Time.size, dtype="int32" )

##  Set up arrays A and B.
##  Each array is a zero or one indicating if a particle resides there.

A   = np.zeros( N, dtype="int32" )
B   = np.zeros( N, dtype="int32" )

##  Populate arrays A and B.
##  Use variables na and nb to be the number left to add to A and B.
##  Only fill up spaces that have not been filled in either.

na  = Na
nb  = Nb

while na > 0:

    free        = np.where( A == 0 )[0]
    i           = np.random.randint( 0, free.size, 1 )[0]  ##  1 random number
    A[free[i]]  = 1
    na         -= 1

while nb > 0:

    free        = np.where( (A == 0) & (B == 0) )[0]
    i           = np.random.randint( 0, free.size, 1 )[0]  ##  1 random number
    B[free[i]]  = 1
    nb         -= 1

##  ========================================================================  ##
##  The Ehrenfet Model

##  Search for Poincare cycles ( Na(t) = Na(t=0) ).
##  Count how many times this condition has been met.

poincare_time   = [0]
pt              = 0

##  Perform time iteration.
##  Select a random nummber of particles to swap.
##  Create binary array of particles chosen to be swapped.
##  Only swap particles that have not been swapped yet.
##  To swap, take the absolute value after subtracting 1.
##      1  ->  0,  0 -> 1

for t in Time:

    R       = np.random.randint( R_min, R_max+1, 1 )
    r       = R
    swapped = np.zeros( N, dtype="int32" )

    while r > 0:

        free                = np.where( swapped == 0 )[0]
        i                   = np.random.randint( 0, free.size, 1 )[0]
        swapped[free[i]]    = 1

        A[free[i]]          = np.abs( A[free[i]] - 1 )
        B[free[i]]          = np.abs( B[free[i]] - 1 )
        r                  -= 1

    ##  Take data.
    ##  Check for poincare cycle.
    ##  Display results to the terminal.
    ##  Plot results.

    a           = np.where( A > 0 )[0].size
    b           = np.where( B > 0 )[0].size
    balance[t]  = a - b

    if a == Na:

        poincare_time.append( t - pt )
        pt  = t

    print(
        "\t",
        "Time:  ", t, ( 7 - len(str(t))) * " ",
        "Balance:  ", balance[t], ( 7 - len(str(balance[t])) ) * " ",
        "P Cycles: ", len(poincare_time) - 1, "    ",
        end="\r"
    );  sys.stdout.flush()

##  ========================================================================  ##
##  Statistics

##  Smooth the data.

smoothed    = np.array( np.copy( balance ) )
weights     = np.zeros( balance.size )

for i in range( 1, smoothed.size - 1 ):

    weights = np.exp(
        -.5 * ( (Time[i]-Time) / sm_std )**2
    )

    smoothed[i] = np.average( balance, weights=weights )

##  Calculate the equilibrium time.
##  This will here be defined as the first time at which
##  the |balance| < median( |balance| ).

abs_balance = np.abs(smoothed)
min_balance = np.median( abs_balance )

i   = 0

while True:

    if abs_balance[i] <= np.median( abs_balance[i:] ):

        eq_time = Time[i]
        break

    elif i >= Time.size:

        eq_time = Time[-1]
        break

    else:

        i  += 1

##  ========================================================================  ##
##  Plot Setup

mean    = np.mean( balance )
median  = np.median( np.abs(balance) )

##  Create figure.
##  Plot the zero line across the x-axis.

Figure  = pyplot.figure()
Ax      = Figure.add_subplot( 111 )

#Ax.set_xlim( 0, net_time )
#Ax.set_ylim( - mean - 3 * median, np.max(balance) )

title   = "".join([
    "$N_A(t_0)$: ", str(Na),    ( 9 - len( str(Na) ) ) * " ",
    "$N_B(t_0)$: ", str(Nb),    ( 9 - len( str(Nb) ) ) * " ",
    "$R_{min}$: ",  str(R_min), ( 9 - len( str(Nb) ) ) * " ",
    "$R_{max}$: ",  str(R_max), ( 9 - len( str(Nb) ) ) * " ",
    "$t_{eq}$:  ",  str(eq_time),  ( 9 - len( str(Nb) ) ) * " ",
])

Ax.set_xlabel( "Time" )
Ax.set_ylabel( "$N_A(t) - N_B(t)$")
Ax.set_title( title )

Ax.plot( Time, balance, marker, ms=ms )
Ax.plot( Time, smoothed, "g", ms=5 )
Ax.plot( Time, np.zeros(Time.size), "k", ms=1 )
Ax.plot( [eq_time, eq_time], [-Na, Na], "r--" )

#Ax.set_xlim( 0, 3*eq_time )

if show is True:
    pyplot.show()

##  Write data to data file.

if write is True:

    out_file    = "Data.dat"
    out_dtype   = {
        "names":    ["Na", "Nb", "R_min", "R_max", "t_eq", "t_p"],
        "formats":  ["i4", "i4", "i4", "i4", "i4", "i4"],
    }
    d_string    = Io.get_dstring( out_dtype )
    out_line    = (Na, Nb, R_min, R_max, eq_time, np.mean(poincare_time))

    out_stream  = open( out_file, "a" )
    out_stream.write("\n")
    out_stream.write( d_string % out_line )
    out_stream.close()

##  ========================================================================  ##

print()
print( "\tFinished!\n" )
