Voronoi diagrams
=================

The -v switch produces the Voronoi diagram of a vertex set in files suffixed
.v.node and .v.edge. In this example, the file dots.node is input, and its
Voronoi diagram is written to dots.1.v.node and dots.1.v.edge. These are
ordinary .node and .edge format files, containing the Voronoi vertices and
edges, respectively. Some of the edges are infinite rays. 

.. plot:: plot/voronoi.py

This implementation does not use exact arithmetic to compute the Voronoi
vertices, and does not check whether neighboring vertices are identical. Be
forewarned that if the Delaunay triangulation is degenerate or near-degenerate,
the Voronoi diagram may have duplicate vertices, crossing edges, or infinite
rays whose direction vector is zero. The result is a valid Voronoi diagram only
if Triangle's output is a true Delaunay triangulation with no holes. The
Voronoi output is usually meaningless (and may contain crossing edges and other
pathology) if the output is a constrained Delaunay triangulation (CDT) or a
conforming constrained Delaunay triangulation (CCDT), or if it has holes or
concavities. If the triangulation is convex and has no holes, this can be fixed
by using the -D switch (in conjunction with a refinement switch, like -q0) to
ensure that a conforming Delaunay triangulation is constructed. 