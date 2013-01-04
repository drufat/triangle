Refining preexisting meshes
===========================

The -r switch causes a mesh (.node and .ele files) to be read and refined. If
the -p switch is also used, a .poly file is read and used to specify edges that
are constrained and cannot be eliminated (although they can be divided into
smaller edges) by the refinement process.

When you refine a mesh, you generally want to impose tighter quality
constraints. One way to accomplish this is to use -q with a larger angle, or -a
followed by a smaller area than you used to generate the mesh you are refining.
In order to simplify the maintenance of a sequence of successively refined
meshes, all files written by Triangle have iteration numbers in their
filenames; the iteration number of each mesh is one greater than that of the
mesh it was created from. In the example below, the input mesh (which you saw
created on the Delaunay triangulation page) has iteration number one, and
consists of the files box.1.node and box.1.ele.