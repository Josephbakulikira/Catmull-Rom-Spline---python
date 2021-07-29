from constants import alpha

alpha = 0.5
def CatmulRomSpline(points, nPoints=50)
    # Parametric constant: 0.5 for the centripetal spline, 0.0 for the uniform spline, 1.0 for the chordal spline.
    
    alpha = 0.5
    # Premultiplied power constant for the following tj() function.
    alpha = alpha/2
    def tj(ti, Pi, Pj):
        return ((Pj.x-Pi.x)**2 + (Pj.y-Pi.y)**2)**alpha + ti

    # Calculate t0 to t4
    t0 = 0
    t1 = tj(t0, P0, P1)
    t2 = tj(t1, P1, P2)
    t3 = tj(t2, P2, P3)
