"""
This will create config file for VINA
Options
--type all|receptor]res1,res2,res3
--config receptor.config.txt


"""
import os as OS
import glob as FILE_SEARCH
import argparse as ARGUMENT

from scripts.config import Configuration
from scripts.logger import Logger



def main():
  file_dir = OS.path.dirname(OS.path.abspath(__file__))
  store_dir = OS.path.expanduser("~/Desktop")
  parser = ARGUMENT.ArgumentParser(prog='VINA Grid Calculator')
  parser.add_argument('-b', '--base', nargs = 1, default = [store_dir], help = 'Base directory for structure files or run the program from the base dir, [default: %(default)s]')
  parser.add_argument('-r', '--residues', nargs = "*", default = [], help = 'Residues to use for parameter file generation, default all')
  parser.add_argument('-c', '--config', nargs = 1, default = ["config.txt"], help = 'Config File Name, [default: %(default)s]')
  parser.add_argument('-s', '--structures', nargs = "*", default = [f"{file_dir}{OS.sep}tests/pdbs/2mps.pdb"], help = 'Provide structure PDB files for grid calculation. [default: %(default)s].')
  parser.add_argument('-d', '--destination', nargs = 1, default = [f"{store_dir}{OS.sep}VINA_CONFIG"], help = 'Destination directory to store the config file. [default: %(default)s].')
  args = parser.parse_args()
  PARAMS = vars(args)

  DEBUGGER = Logger(level = 2)
  DEBUGGER.debug(PARAMS)

  """
  Create destination directory if doesn't exist

  """

  if not OS.path.exists(PARAMS.get("destination")[0]):
    OS.makedirs(PARAMS.get("destination"))

  """
  Discover all the files in the given base directory based on the files
  """

  base_path = PARAMS.get("base", "")[0]
  structure_pattern = PARAMS.get("structures", [])
  structure_list = []
  for _pat in structure_pattern:
    _nr = list(FILE_SEARCH.glob(f"{base_path}{OS.sep}{_pat}", recursive=True))
    structure_list.extend(_nr)

  # python vina.py -s *.pdb -b "D:\Desktop\VINA-Grid-Test" -d "D:\Desktop\VINA-Grid-Test"
  DEBUGGER.debug(structure_list)
  for _rec in structure_list:
    DEBUGGER.debug(_rec)
    config = Configuration()
    c_p = config.write(**{
      "file": f"{_rec}",
      "residues": PARAMS.get("residues"),
      "output_file_name": str(PARAMS.get("config")[0]),
      "output_file_location": PARAMS.get("destination")[0],
    })
    DEBUGGER.debug(f"Wrote {c_p}")

if __name__ == "__main__":
  main()
