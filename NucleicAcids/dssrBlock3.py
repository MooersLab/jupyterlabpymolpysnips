cmd.do('reinitialize;')
cmd.do('run "/Users/blaine/.pymol/startup/dssr_block.py";')
cmd.do('fetch 2n2d, async=0;')
cmd.do('dssr_block  2n2d, 0;')
cmd.do('set all_states;')
