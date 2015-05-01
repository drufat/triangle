def compare(plt, A, B): 
    ax1 = plt.subplot(121, aspect='equal')
    plot(ax1, **A)
    ax2 = plt.subplot(122, sharex=ax1, sharey=ax1)
    plot(ax2, **B)
    
def plot(ax, **kw):

    vertices(ax, **kw)
    ax.axes.set_aspect('equal')

    if 'segments' in kw: segments(ax, **kw)
    if 'triangles' in kw: triangles(ax, **kw)
    if 'holes' in kw: holes(ax, **kw)
    if 'edges' in kw: edges(ax, **kw)
        
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

def vertices(ax, **kw):    
    verts = kw['vertices']
    ax.scatter(*verts.T, color='k')  
    if 'labels' in kw:
        for i in range(verts.shape[0]):
            ax.text(verts[i,0], verts[i,1], str(i))
    if 'markers' in kw:
        vm = kw['vertex_markers']
        for i in range(verts.shape[0]):
            ax.text(verts[i,0], verts[i,1], str(vm[i]))

def segments(ax, **kw):
    verts = kw['vertices']    
    segs = kw['segments']
    for beg, end in segs:
        x0, y0 = verts[beg, :]
        x1, y1 = verts[end, :]
        ax.fill([x0, x1], [y0, y1], 
                facecolor='none', edgecolor='r', linewidth=3,
                zorder=0)

def triangles(ax, **kw):
    verts = kw['vertices']
    ax.triplot(verts[:,0], verts[:,1], kw['triangles'],'ko-')

def holes(ax, **kw): 
    ax.scatter(*kw['holes'].T, marker='x', color='r')
    
def edges(ax, **kw):
    """
    Plot regular edges and rays (edges whose one endpoint is at infinity)
    """
    verts = kw['vertices']
    edges = kw['edges']
    for beg, end in edges:
        x0, y0 = verts[beg, :]
        x1, y1 = verts[end, :]
        ax.fill([x0, x1], [y0, y1], facecolor='none', edgecolor='k', linewidth=.5)

    if ('ray_origins' not in kw) or ('ray_directions' not in kw):
        return
    
    lim = ax.axis()
    ray_origin = kw['ray_origins']
    ray_direct = kw['ray_directions']
    for (beg, (vx, vy)) in zip(ray_origin.flatten(), ray_direct):
        x0, y0 = verts[beg, :]
        scale = 100.0 # some large number
        x1, y1 = x0 + scale*vx, y0 + scale*vy
        ax.fill([x0, x1], [y0, y1], facecolor='none', edgecolor='k', linewidth=.5)
    ax.axis(lim) # make sure figure is not rescaled by ifinite ray
