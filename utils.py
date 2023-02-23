import pandas as pd
import numpy as np
import rdkit
from rdkit import Chem
from rdkit.Chem import Descriptors
from mordred import Calculator, descriptors

def smiles2desc(smiles_list):
    mols = [Chem.MolFromSmiles(smiles) for smiles in smiles_list]
    calc = Calculator(descriptors, ignore_3D=True)
    descriptor = calc.pandas(mols)[['MW', 'FilterItLogS']]
    return descriptor

def mol2desc(mols):
    calc = Calculator(descriptors, ignore_3D=True)
    descriptor = calc.pandas(mols)[['MW', 'FilterItLogS']]
    return descriptor