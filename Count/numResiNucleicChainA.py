cmd.do('sel = 'chain A and polymer.nucleic'; print(len(set([(i.resi, i.resn) for i in cmd.get_model(sel).atom])));')
