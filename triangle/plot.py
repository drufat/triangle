from triangle import *

def plot(plt, pts, **kwargs):
    """
    Demonstrate the trinagulation library.
    """
    
    pnts, triangles = triangulate(pts, **kwargs)
    
    ax1 = plt.subplot(121, aspect='equal')
    plt.scatter(pts[:,0], pts[:,1])
    
    plt.subplot(122, sharex=ax1, sharey=ax1)
    plt.triplot(pnts[:,0], pnts[:,1], triangles,'bo-')


