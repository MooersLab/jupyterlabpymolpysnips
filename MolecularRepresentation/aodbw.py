cmd.do('set_color oxygen, [1.0,0.4,0.4];')
cmd.do('set_color nitrogen, [0.5,0.5,1.0];')
cmd.do('remove solvent;')
cmd.do('as spheres;')
cmd.do('util.cbaw;')
cmd.do('bg white;')
cmd.do('gscale();')
cmd.do('set light_count,10;')
cmd.do('set spec_count,1;')
cmd.do('set shininess, 10;')
cmd.do('set specular,0.25;')
cmd.do('set ambient,0;')
cmd.do('set direct,0;')
cmd.do('set reflect,1.5;')
cmd.do('set ray_shadow_decay_factor, 0.1;')
cmd.do('set ray_shadow_decay_range, 2;')
cmd.do('set depth_cue, 0;')
cmd.do('ray;')
