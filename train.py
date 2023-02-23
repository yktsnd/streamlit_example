from sklearn.ensemble import RandomForestRegressor
import numpy as np
import pandas as pd
import rdkit
from rdkit import Chem
from rdkit.Chem import Descriptors
from mordred import Calculator, descriptors
import pickle
import utils

def make_data(sdf):
    mols = [m for m in Chem.SDMolSupplier(sdf) if m !=None]
    X = utils.mol2desc(mols)
    y = [float(m.GetProp('SOL')) for m in mols]
    return X, y

sdf = './solubility.train_.sdf'
rf = RandomForestRegressor()
print('Load Data...')
X, y = make_data(sdf)
print('Fitting...')
rf.fit(X, y)
pickle.dump(rf, open('rf.pkl', 'wb'))


