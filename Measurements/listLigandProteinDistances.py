from pymol import cmd
"""
Find all distances betwen all ligand atoms and all protein atoms. 

Adapted and updated from script by Dan Kulp posted here
https://sourceforge.net/p/pymol/mailman/message/10097804/

There are probably better solutions like finding just the 
distances to proein atoms within a certain distance from 
the ligand.

Due to the nested for loops, this script is takes several second
to run on a medium-sized human protein. This script is a 
good candidate for vectorization. 

It is also a good candiate for becoming a function and a shortcut. 

"""

# customize these lines to your protein.
cmd.fetch("6NEC")
cmd.select("prot","not resn XIN and not resn HOH and not chain C")
cmd.select("lig", "resn XIN and not chain C")

dist_list = {
pro_atoms = cmd.get_model("prot")
lig_atoms = cmd.get_model("lig")

for l_at in lig_atoms.atom:
    for p_at in pro_atoms.atom:
        dist_list[str(l_at.resn) +
                     ":" +
                      str(l_at.resi) +
                      " " +
                      l_at.name +
                      " ---- " + 
                      str(p_at.resn) +
                      ":" +
                      str(p_at.resi) +
                      " " +
                      p_at.name] = cmd.dist("foo", 
                                            "index " +
                                            str(l_at.index),"index " + str(p_at.index))
        cmd.delete("foo")
print("List of all pairwise ligand--protein atom-atom distances:")
# [print("Distance of " + d + " is " + str(dist_list[d])) for d in dist_list.keys()]

# More compact print statement. Need an f-string format statement.
[print( d + " " + str(dist_list[d])) for d in dist_list.keys()]
