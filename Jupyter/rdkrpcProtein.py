cmd.do('from rdkit.Chem import PyMol;')
cmd.do('')
cmd.do('Usage=""""Start pymol from command line with -R flag.')
cmd.do('Select the pymol.python kernel in Jupyter notebook. """;')
cmd.do('')
cmd.do('s = PyMol.MolViewer();')
cmd.do('du = s.server.do;')
cmd.do('du('rein; bg_color white; fetch 1lw9, type=pdb, async=0, show;nb_spheres; set_view (0.46,-0.28,-0.84,0.74,-0.41,0.54,-0.49,-0.87,0.02,0.0,0.0,\')
cmd.do(' -155.16,35.13,11.48,9.72,122.33,187.99,-20.0);');')
cmd.do('s.GetPNG(preDelay=3);')
cmd.do('du('png T4L600dpi.png, dpi=600');')
