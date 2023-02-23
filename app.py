import streamlit as st
import pandas as pd
import numpy as np
import rdkit
from rdkit import Chem
from rdkit.Chem import Descriptors
from mordred import Calculator, descriptors
import matplotlib.pyplot as plt
import utils
import pickle


model = pickle.load(open('./rf.pkl', 'rb'))
@st.cache
def predict_solubility(X):
    solubility = model.predict(X)
    return solubility[0]

st.title("Solubility Predictor")

smiles = st.text_input("Enter the SMILES of a compound:")

if smiles:
    X = utils.smiles2desc([smiles])
    solubility = predict_solubility(X)
    st.write(f"The predicted solubility is: {solubility:.2f}")

    X['Solubility'] = solubility

    st.write("DataFrame")
    st.dataframe(X)