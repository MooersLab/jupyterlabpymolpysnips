cmd.do('delete all;')
cmd.do('# Fetch the coordinates. Need internet connection.;')
cmd.do('fetch 4dgr, async=0;')
cmd.do('# Fetch the electron density map.;')
cmd.do('fetch 4dgr, type=2fofc,async=0;')
cmd.do('# create a selection out of the glycan;')
cmd.do('select LongGlycan, resi 469:477;')
cmd.do('orient LongGlycan;')
cmd.do('remove not LongGlycan;')
cmd.do('remove name H*;')
cmd.do('isosurface 2fofcmap, 4dgr_2fofc, 1, LongGlycan, carve = 1.8;')
cmd.do('color density, 2fofcmap; ')
cmd.do('show sticks;')
cmd.do('show spheres;')
cmd.do('set stick_radius, .07;')
cmd.do('set sphere_scale, .19;')
cmd.do('set sphere_scale, .13, elem H;')
cmd.do('set bg_rgb=[1, 1, 1];')
cmd.do('set stick_quality, 50;')
cmd.do('set sphere_quality, 4;')
cmd.do('color gray85, elem C;')
cmd.do('color red, elem O;')
cmd.do('color slate, elem N;')
cmd.do('color gray98, elem H;')
cmd.do('set stick_color, gray50;')
cmd.do('set ray_trace_mode, 1;')
cmd.do('set ray_texture, 2;')
cmd.do('set antialias, 3;')
cmd.do('set ambient, 0.5;')
cmd.do('set spec_count, 5;')
cmd.do('set shininess, 50;')
cmd.do('set specular, 1;')
cmd.do('set reflect, .1;')
cmd.do('set dash_gap, 0;')
cmd.do('set dash_color, black;')
cmd.do('set dash_gap, .15;')
cmd.do('set dash_length, .05;')
cmd.do('set dash_round_ends, 0;')
cmd.do('set dash_radius, .05;')
cmd.do('set_view (0.34,-0.72,0.61,0.8,0.56,0.22,-0.51,0.4,0.77,0.0,0.0,-81.31,44.64,-9.02,58.62,65.34,97.28,-20.0);')
cmd.do('preset.ball_and_stick("all",mode=1);')
cmd.do('draw;')
