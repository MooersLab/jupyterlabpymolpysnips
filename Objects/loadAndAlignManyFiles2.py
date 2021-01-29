cmd.do('#  Yes, this construct is a list comprehension inside a list comprehension!;')
cmd.do('run ~/Scripts/optAlignRNA.py;')
cmd.do('[[optAlignRNA(x, y) for x in cmd.get_names()] for y in cmd.get_names()];')
