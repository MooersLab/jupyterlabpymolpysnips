cmd.do('fetch 3nd4, 3nd4_2fofc, type=2fofc, async=0;')
cmd.do('# Render and display a contour of this map as a chicken wire representation.;')
cmd.do('isosurface 2fofcmap, 3nd4_2fofc, 1, 3nd4, carve = 1.8;')
