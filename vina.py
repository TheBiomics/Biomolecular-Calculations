"""
This will create config file for VINA
Options
--type all|receptor]res1,res2,res3
--config receptor.config.txt


"""
import os as OS

import argparse as ARGUMENT
import sys as SYSTEM
from scripts.config import Configuration


def main():
  # parser=ARGUMENT.ArgumentParser()
  # parser.add_argument('--type', help='Type of Config File Generation')
  # parser.add_argument('--config', help='Config File Name')
  # parser.add_argument('--files', help='Config File Name')
  # _files = SYSTEM.argv
  # _files.pop(0) 
  # _files_count = len(_files)
  # print(_files)
  # if not _files_count:
  #   print("""
  #     Please provide atleast one PDB File location or
  #     execute this script in the directory where PDB file resides
  #   """)
  file_dir = OS.path.dirname(OS.path.abspath(__file__))
  _file_path = f"{file_dir}{OS.sep}tests/pdbs/2mps.pdb"
  config = Configuration()
  config.write(**{"file": _file_path})


if __name__ == "__main__":
  main()