cmd.do('sel = 'polymer.nucleic'; print(len(set([(i.resi, i.resn) for i in cmd.get_model(sel).atom])));')
