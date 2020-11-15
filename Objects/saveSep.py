cmd.do('from pymol import cmd')
cmd.do('import glob')
cmd.do('import re')
cmd.do('')
cmd.do('def saveSep(prefix=''):')
cmd.do('  """')
cmd.do('  save_sep <prefix>')
cmd.do('')
cmd.do('  saves multiple objects into multiple files using an optional prefix name.')
cmd.do('')
cmd.do('  e.g. save_sep prefix')
cmd.do('  """')
cmd.do('  obj_list = cmd.get_names("all")')
cmd.do('')
cmd.do('  if obj_list:')
cmd.do('    for i in range(len(obj_list)):')
cmd.do('      obj_name = "%s%s.pdb" % (prefix, obj_list[i])')
cmd.do('      cmd.save(obj_name, obj_list[i])')
cmd.do('      print("Saving %s" %  obj_name)')
cmd.do('  else:')
cmd.do('    print("No objects found")')
cmd.do('    ')
cmd.do('cmd.extend('saveSep',saveSep)')
