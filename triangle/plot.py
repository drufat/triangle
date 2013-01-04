from triangle import triangulate

def demo(plt, pts, **kwargs):    
    
    pnts, triangles = triangulate(pts, **kwargs)

    ax1 = plt.subplot(121, aspect='equal')
    plot(ax1, vertices=pts)
    
    ax2 = plt.subplot(122, sharex=ax1, sharey=ax1)
    plot(ax2, vertices=pnts, triangles=triangles)
    
def plot(ax, **kw):

    verts = kw['vertices']
    ax.scatter(*verts.T, color='k')    
    
    if 'segments' in kw:
        segs = kw['segments']
        for beg, end in segs:
            x0, y0 = verts[beg, :]
            x1, y1 = verts[end, :]
            ax.fill([x0, x1], [y0, y1], facecolor='none', edgecolor='k', linewidth=.5)
    
    if 'holes' in kw:
        ax.scatter(*kw['holes'].T, marker='x', color='r')
    
    if 'triangles' in kw:
        ax.triplot(verts[:,0], verts[:,1], kw['triangles'],'ko-')
        
    ax.axes.set_aspect('equal', 'datalim')
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

