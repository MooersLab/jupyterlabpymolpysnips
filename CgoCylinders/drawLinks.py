cmd.do('# Requires draw_links.py http://pldserver1.biochem.queensu.ca/~rlc/work/pymol/draw_links.py by Robert Campbell')
cmd.do('# To connect the alpha carbons of residue 1 with 10, 6 with 16, 7  with 17 and 8 with 18.')
cmd.do('draw_links mol1 & chain A & name  CA & resi 1+6+7+8, mol1 & chain A& name CA & resi 10+16+17+18 ')
