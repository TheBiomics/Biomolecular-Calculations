import urllib.request as URL
import os as OS
from Bio.PDB import PDBParser
import pandas as PD
import numpy as NP
import math as MATH

PDB_DOWNLOAD_DIR = fr".{OS.sep}pdbs"
if not OS.path.exists(PDB_DOWNLOAD_DIR):
  OS.makedirs(PDB_DOWNLOAD_DIR)

def unit_vector(vector):
  return vector/NP.linalg.norm(vector)

def angle_between(v1, v2):
  v1_u = unit_vector(v1)
  v2_u = unit_vector(v2)
  return NP.arccos(NP.clip(NP.dot(v1_u, v2_u), -1.0, 1.0))*(180/MATH.pi)

def calculate_angle(pdb_df, fci, frid, sci, srid):
  _first_ca = pdb_df[pdb_df.chain_id.isin(fci) & pdb_df.residue_id.isin(frid) & pdb_df.atom_id.isin(['CA'])].copy()
  _first_ca = _first_ca.reset_index(drop=True)
  _first_ca = _first_ca.loc[0].to_dict()

  _second_ca = pdb_df[pdb_df.chain_id.isin(sci) & pdb_df.residue_id.isin(srid) & pdb_df.atom_id.isin(['CA'])].copy()
  _second_ca = _second_ca.reset_index(drop=True)
  _second_ca = _second_ca.loc[0].to_dict()

  return angle_between(_first_ca.get('coord'), _second_ca.get('coord'))

def get_pdb(_pdb):
  _file_path = f"{PDB_DOWNLOAD_DIR}/{_pdb}.pdb"

  if not OS.path.exists(_file_path):
    URL.urlretrieve(f"http://files.rcsb.org/download/{_pdb}.pdb", _file_path)

  parser = PDBParser()
  structure = parser.get_structure("PDB", _file_path)
  _dictionary = []

  for chain in structure.get_chains():
    for residue in chain:
      for atom in residue:
        _dictionary.append({
          "chain_id": chain.id,
          "residue_id": residue.id[1],
          "residue_name": residue.resname,
          "atom_id": atom.id,
          "atom_element": atom.element,
          "atom_mass": atom.mass,
          # "x": atom.coord[0],
          # "y": atom.coord[1],
          # "z": atom.coord[2],
          "coord": atom.coord
        })

  return PD.DataFrame(_dictionary)

_pdb = get_pdb("1FQV")

_first__chain = ["A"] # Chain ID
_first__resid = [107] # Residue ID

_second__chain = ["A"] # Chain ID
_second__resid = [148] # Residue ID

calculate_angle(_pdb, _first__chain, _first__resid, _second__chain, _second__resid)
