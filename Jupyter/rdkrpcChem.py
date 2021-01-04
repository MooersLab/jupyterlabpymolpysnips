import os;
import rdkit;
from rdkit import Chem;
from rdkit.Chem import AllChem;
from rdkit.Chem import PyMol;

s = PyMOL.MolViewer();
mol = Chem.MolFromSmiles \
   ('CCOCCn1c(C2CC[NH+](CCc3ccc(C(C)(C)C(=O)[O-])cc3)CC2)nc2ccccc21');
mol = AllChem.AddHs(mol);
AllChem.EmbedMolecule(mol);
AllChem.MMFFOptimizeMolecule(mol);
s.ShowMol(mol, name = 'bilastine', showOnly = False);
s.Zoom('bilastine');
s.SetDisplayStyle('bilastine', 'sticks');
s.GetPNG(preDelay=5);

