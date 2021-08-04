from rdkit.Chem.Draw import rdMolDraw2D
from rdkit.Chem import AllChem
from rdkit import Chem

# Adapted from Oliver Scott at
# https://stackoverflow.com/questions/65823691/how-would-you-convert-a-large-sdf-file-of-chemical-compounds-into-individual-fil

img_size = (600, 600)
supplier =  Chem.SDMolSupplier('resources/dataset/dataset.sdf')
for mol in supplier:
    AllChem.Compute2DCoords(mol)
    property = mol.GetProp('chembl_pref_name')
    d = rdMolDraw2D.MolDraw2DCairo(*img_size)
    d.DrawMolecule(mol)
    d.FinishDrawing()
    d.WriteDrawingText(f'resources/images/{property}.png')