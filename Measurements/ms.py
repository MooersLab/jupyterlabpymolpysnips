cmd.do('fetch 3nd3, name=3nd3, type=pdb, async=0;')
cmd.do('select temp, 3nd3 and chain A;')
cmd.do('run /Users/blaine-mooers/Scripts/PyMOLScripts/msms_pymol.py;')
cmd.do('calc_msms_area temp;')
