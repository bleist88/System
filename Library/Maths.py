
import numpy as np
import matplotlib.pyplot as pyplot

##  ========================================================================  ##

##  Histogram Function

def hist( sample, dx=None, bins=None, min=None, max=None ):

    ##  Use the arguments to define the space.

    x_min   = min
    x_max   = max

    if x_min is None:
        x_min   = np.min( sample )

    if x_max is None:
        x_max   = np.max( sample )

    if dx is None and bins is not None:
        dx  = (x_max - x_min) / bins

    if dx is None and bins is None:
        dx  = .1 * np.std( sample )

    ##  Create arrays.

    x   = np.arange( x_min, x_max + dx, dx )
    N   = np.zeros( x.size, dtype="int64" )

    ##  Count the number of sample points in each bin.

    for i in range( x.size - 1 ):

        N[i]    = np.where( (sample >= x[i]) & (sample <= x[i+1]) )[0].size

    return  x, N

##  ========================================================================  ##

##  Gaussian Smoothing Function

def smooth( x, y, std, trim=1 ):

    Y   = np.zeros( y.size )

    for i in range( trim, x.size - trim ):

        weights = np.exp( -.5 * ((x - x[i]) / std)**2 )
        Y[i] = np.average( y, weights=weights )

    return  Y

##  ========================================================================  ##

##  Gaussian Interpolation Function

def interpolate( x, y, dx ):

    X       = np.arange( np.min(x), np.max(x) + dx, dx )
    Y       = np.zeros( X.size )
    Y[0]    = y[0]
    Y[-1]   = y[-1]

    slope       = np.zeros( x.size )
    slope[1:]   = (y[1:] - y[:-1]) / (x[1:] - x[:-1])

    ##  Loop through all X points.

    for i in range( 1, X.size ):
        for j in range( x.size - 1 ):
            if X[i] >= x[j] and X[i] < x[j+1]:

                ##  Create gaussian weights to average slope.

                d1      = X[i] - x[j]
                d2      = x[j+1] - X[i]
                S       = (d2 * slope[j] + d1 * slope[j+1]) / ( d1 + d2 )

                ##  Estimate the point based on the slopes.

                Y[i]    = y[j] + S * d1

    return  X, Y

##  ========================================================================  ##

##  Convolution Filtering Function.

def convolve( x, y, F ):

    ##  Create a longer y so that F can completely pass through.
    ##  Y outside of y is set to 0.

    Y   = np.zeros( y.size + 2 * F.size )
    C   = np.zeros( y.size + 2 * F.size )
    Y[ F.size : F.size + y.size ]   = y

    ##  Convolve F with Y.

    for i in range( C.size - F.size + 1 ):

        C[i]    = np.sum( F * Y[ i : F.size + i ] )

    C   = C[ F.size : F.size + y.size ]

    return  C

##  ========================================================================  ##

##  Fold and integrate two functions.

def fold( x1, y1, x2, y2, X=None ):

    ##  Use the SED space if X is not specified.

    if X is not None:

        X   = x1

    ##  Ensure that the SED and filter are on the same space.

    if x1 != x2:

        Y1      = np.interp( X, x1, y1 )
        Y2      = np.interp( X, x2, y2 )

    pyplot.plot( X, Y1, "k" )
    pyplot.plot( X, Y2, "b" )
    pyplot.plot( X, Y1 * Y2 )
    pyplot.show()

    ##  Integrate the Filter with the SED to obtain the flux.

    flux        = np.trapz( Y1 * Y2, x=X )

    return  flux

##  ========================================================================  ##

##  Cumulative Distribution Function

def cdf( x, y ):

    Y   = np.zeros( y.size )

    for i in range( x.size ):

        Y[i]    = np.trapz( y[:i], x=x[:i] )

    return  Y
