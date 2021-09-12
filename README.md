# Biomolecular-Calculations
Calculation of Biomolecular Dimensions for AutoDock VINA Docking and Other Operations

# Usage

## Using script for pdbs in a directory

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

# Features

* Calculates grid size of a given PDB
- Using coordinates
- Adding spacing around the coordinates

* Calculates grid around selected residues
- Fitting the coordinates
- Adding spacing around the coordinates

# Scripting

- config.py
* Creates config file for AutoDock VINA


## Current Development Script
Python 3.9.5

# Future Improvements
* Conda environment integration
* Cross Platform Support (Currently being developed for windows platform)
* Commandline execution
* Create config files for rDock


# TODO List
Edit this list or provide the requirement through comments

* Testing
* Time taken for calculation
* Adding references for different options and suitable options

# Ref
https://www.cgl.ucsf.edu/chimera/docs/UsersGuide/tutorials/pdbintro.html
https://github.com/schrodinger/pymol-open-source/blob/master/INSTALL
https://pymolwiki.org/index.php/Windows_Install


# Managing using conda

```
conda env export --name GridCalculator --no-builds > docs/GridCalculator.yml
conda env create --file docs/GridCalculator.yml
```

# Installations

```
pip install biopython

```
