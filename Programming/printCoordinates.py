cmd.do('stored.coords = []; ')
cmd.do('iterate_state 1, (resi 101), stored.coords.append([x,y,z]); ')
cmd.do('[print(i) for i in stored.coords];')
