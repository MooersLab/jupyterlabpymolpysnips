cmd.do('stored.coords = []; iterate_state 1, (resi 101), stored.coords.append([x,y,z]); ')
cmd.do('stored.names = [];  iterate_state 1, (resi 101), stored.names.append([name]);')
cmd.do('stored.names3 = [tuple(i) for i in stored.names];')
cmd.do('[print(i,j) for i,j in(zip(stored.names3, stored.coords)];')
