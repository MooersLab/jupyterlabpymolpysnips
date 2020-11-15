cmd.do('from pymol import cmd')
cmd.do('"""')
cmd.do('Find all distances betwen all ligand atoms and all protein atoms. ')
cmd.do('')
cmd.do('Adapted and updated from script by Dan Kulp posted here')
cmd.do('https://sourceforge.net/p/pymol/mailman/message/10097804/')
cmd.do('')
cmd.do('There are probably better solutions like finding just the ')
cmd.do('distances to proein atoms within a certain distance from ')
cmd.do('the ligand.')
cmd.do('')
cmd.do('Due to the nested for loops, this script is takes several second')
cmd.do('to run on a medium-sized human protein. This script is a ')
cmd.do('good candidate for vectorization. ')
cmd.do('')
cmd.do('It is also a good candiate for becoming a function and a shortcut. ')
cmd.do('')
cmd.do('"""')
cmd.do('')
cmd.do('# customize these lines to your protein.')
cmd.do('cmd.fetch("6NEC")')
cmd.do('cmd.select("prot","not resn XIN and not resn HOH and not chain C")')
cmd.do('cmd.select("lig", "resn XIN and not chain C")')
cmd.do('')
cmd.do('dist_list = {')
cmd.do('pro_atoms = cmd.get_model("prot")')
cmd.do('lig_atoms = cmd.get_model("lig")')
cmd.do('')
cmd.do('for l_at in lig_atoms.atom:')
cmd.do('    for p_at in pro_atoms.atom:')
cmd.do('        dist_list[str(l_at.resn) +')
cmd.do('                     ":" +')
cmd.do('                      str(l_at.resi) +')
cmd.do('                      " " +')
cmd.do('                      l_at.name +')
cmd.do('                      " ---- " + ')
cmd.do('                      str(p_at.resn) +')
cmd.do('                      ":" +')
cmd.do('                      str(p_at.resi) +')
cmd.do('                      " " +')
cmd.do('                      p_at.name] = cmd.dist("foo", ')
cmd.do('                                            "index " +')
cmd.do('                                            str(l_at.index),"index " + str(p_at.index))')
cmd.do('        cmd.delete("foo")')
cmd.do('print("List of all pairwise ligand--protein atom-atom distances:")')
cmd.do('# [print("Distance of " + d + " is " + str(dist_list[d])) for d in dist_list.keys()]')
cmd.do('')
cmd.do('# More compact print statement. Need an f-string format statement.')
cmd.do('[print( d + " " + str(dist_list[d])) for d in dist_list.keys()]')
