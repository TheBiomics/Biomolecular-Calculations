# Biomolecular Calculator
Calculation of Biomolecular Dimensions

# Usage

## Using script for pdbs in a directory to create vina config files in bulk

```
# Single File In a Directory for Specific residues (residues are optional, if not provided it will work for whole the structure)
python /path/to/vina.py -b /path/to/base/directory -s xyz.pdb -res ALA ASN TRP

# Using File Name pattern(s) or using multiple files, both will work
python /path/to/vina.py -b /path/to/base/directory -s *.pdb *xyz.pdb m*.pdb -res ALA ASN TRP

# Giving Spacing
python /path/to/vina.py -b /path/to/base/directory -s *.pdb *xyz.pdb m*.pdb -res HETATM -spc 10

```

## Check Options or parameters
python /path/to/vina.py -h
python /path/to/vina.py --help

## Setting different VINA Option
python /path/to/vina.py [OTHER OPTIONS] --exhaustiveness 15 --cpu 2

# Features for calculating grid for autodock VINA

* Calculates grid size of a given PDB 
- Using coordinates
- Adding spacing around the coordinates

* Calculates grid around selected residues
- Fitting the coordinates
- Adding spacing around the coordinates


# Ref and downloades
* https://www.cgl.ucsf.edu/chimera/docs/UsersGuide/tutorials/pdbintro.html
* https://github.com/schrodinger/pymol-open-source/blob/master/INSTALL
* https://pymolwiki.org/index.php/Windows_Install

# Notes
* Created using Python 3.9.5, not tested with other versions of python
* For any other calculation, feel free to comment

