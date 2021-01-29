cmd.do('fetch 3nd4, type=cif, async=0;')
cmd.do('fetch 3nd4, {1:3nd4_2fofc, type=2fofc, async=0;')
cmd.do('# Render and display a contour of this map as a volume around a selection called LongGlycan.;')
cmd.do('volume 2fofcmap, 3nd4_2fofc, 1, LongGlycan, carve = 1.8;')
