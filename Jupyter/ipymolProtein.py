# Start pymol in terminal with pymol -R;
# Select pymol.python as kernel in juptyer;
from ipymol import viewer as ipv;
ipv.start() # Start PyMOL RPC server;

ipv.do('fetch 1lw9');
ipv.do('rv');
# The double parentheses are required when set_view is run this way.;
ipv.set_view((-0.13,-0.4,-0.91,0.89,-0.45,0.07,-0.44,-0.8,0.41,0.0,0.0,-182.47,35.13,11.48,9.72,149.64,215.3,-20.0));
ipv.do('AOD');
ipv.png('testipymolT4L.png');

