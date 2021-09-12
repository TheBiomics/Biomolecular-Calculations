"""
This will create config file for VINA

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
  
  CONFIG = Configuration()

  parser.add_argument('-s', '--structures', nargs = "*", default = [f"{file_dir}{OS.sep}tests/pdbs/2mps.pdb"], help = 'Provide structure PDB files for grid calculation. [default: %(default)s].')
  parser.add_argument('-res', '--residues', nargs = "*", default = [], help = '[Optional] Specify residues around which grid will be calculated, default all')
  parser.add_argument('-b', '--base', default = store_dir, help = 'Base directory for structure files or run the program from the base dir, [default: %(default)s]')
  parser.add_argument('-d', '--destination', default = f"{store_dir}{OS.sep}VINA_CONFIG", help = 'Destination directory to store the config file. [default: %(default)s].')
  parser.add_argument('-c', '--config_file', default = "config.txt", help = '[Optional] Config File Name, [default: %(default)s]')
  parser.add_argument('-spc', '--spacing', default = 1, help = 'Additional spacing around the grid, [default: %(default)s]')
  
  # Dynamically add vina configuration Options
  for conf_key in CONFIG.vina_config_keys:
    parser.add_argument(f"--{conf_key}", nargs = None, help = "Check VINA's help for more details.")
  
  args = parser.parse_args()
  PARAMS = vars(args)
  # Filter None
  PARAMS = {key: PARAMS[key] for key in PARAMS.keys() if PARAMS[key] is not None}

  DEBUGGER = Logger(level = 2)
  DEBUGGER.debug(PARAMS)

  """
  Create destination directory if doesn't exist

  """

  if not OS.path.exists(PARAMS.get("destination")):
    OS.makedirs(PARAMS.get("destination"))

  """
  Discover all the files in the given base directory based on the files
  """

  base_path = PARAMS.get("base", "")
  structure_pattern = PARAMS.get("structures", [])
  structure_list = []
  for _pat in structure_pattern:
    _nr = list(FILE_SEARCH.glob(f"{base_path}{OS.sep}{_pat}", recursive=True))
    structure_list.extend(_nr)

  # python vina.py -s *.pdb -b "D:\Desktop\VINA-Grid-Test" -d "D:\Desktop\VINA-Grid-Test" -res TRP ASN

  DEBUGGER.debug(structure_list)
  for _rec in structure_list:
    DEBUGGER.debug(_rec)
    params = {
      "file": f"{_rec}",
    }
    params.update(PARAMS)
    c_p = CONFIG.write(**params)
    DEBUGGER.debug(f"Wrote {c_p}")

if __name__ == "__main__":
  main()
