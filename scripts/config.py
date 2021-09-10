import os as OS
import math as MATH
from typing import final
from Bio.PDB import *

class Configuration():
  def __init__(self) -> None:
    self.output_file_location = OS.path.expanduser("~/Desktop")
    self.output_file_name = "config.txt"
    self.coordinates = []
    self.properties = []
    self.vina_config = []
    self.vina_config = []
    self.params = {}
    pass

  def __set_parameters(self, **params):
    self.params = {
      "receptor": params.get("receptor"),
      "receptor": params.get("ligand"),

      "center_x": self.vina_config.get("center_x"),
      "center_y": self.vina_config.get("center_y"),
      "center_z": self.vina_config.get("center_z"),
      "size_x": self.vina_config.get("size_x"),
      "size_y": self.vina_config.get("size_y"),
      "size_z": self.vina_config.get("size_z"),

      "energy_range": params.get("energy_range", 3),
      "seed": params.get("seed", 41103333),
      "exhaustiveness": params.get("exhaustiveness", 16),
    }
    
    self.output_file_location = params.get("output_file_location", self.output_file_location)
    self.output_file_name = params.get("output_file_name", self.output_file_name)

  def __set_vina_config(self):
    center_x, center_y, center_z = self.properties['center']
    center_x = round(center_x, 4)
    center_y = round(center_y, 4)
    center_z = round(center_z, 4)
    
    """
    VINA has maximum box size of 12.6 nm
    """
    size_x, size_y, size_z = self.properties['size']
    size_x = min(int(size_x), 126)
    size_y = min(int(size_y), 126)
    size_z = min(int(size_z), 126)

    self.vina_config = {
      "center_x": center_x,
      "center_y": center_y,
      "center_z": center_z,
      "size_x": size_x,
      "size_y": size_y,
      "size_z": size_z,
    }

  """
  Writes VINA config Only
  """
  def write(self, **params):
    self.file = params.get("file")
    self.__read_file()
    self.__set_properties()
    self.__set_vina_config()
    self.__set_parameters(**params)

    config = self.params
    final_config = [f"{config_key} = {config[config_key]}\n" for config_key in config.keys() if config[config_key] is not None]

    with open(f"{self.output_file_location}{OS.sep}{self.output_file_name}", "w+", encoding="utf-8") as f:
      f.writelines(final_config)

    pass

  def __read_file(self):
    parser = PDBParser()
    structure = parser.get_structure("PDB", self.file)
    self.coordinates = []
    for atom in structure.get_atoms():
      self.coordinates.append(atom.get_coord())

  def __filter_coordinates(self):
    """
    Filter coordinates to calculate the grid of selected res only
    """
    pass


  def __set_properties(self):
    x_total = 0
    y_total = 0
    z_total = 0

    x_min = 0
    x_max = 0

    y_min = 0
    y_max = 0

    z_min = 0
    z_max = 0
    
    d_x = 0
    d_y = 0
    d_z = 0
    
    for c in self.coordinates:    
      at_x = float(c[0])
      at_y = float(c[1])
      at_z = float(c[2])
      x_total += at_x
      y_total += at_y
      z_total += at_z
      x_min = min(x_min, at_x)
      x_max = max(x_max, at_x)
      y_min = min(y_min, at_y)
      y_max = max(y_max, at_y)
      z_min = min(z_min, at_z)
      z_max = max(z_max, at_z)
    
    center = [x_total/len(self.coordinates), y_total/len(self.coordinates), z_total/len(self.coordinates)]
    size = [(x_max - x_min), (y_max - y_min), (z_max - z_min)]

    for c in self.coordinates:
        d_x += (c[0]-center[0])**2
        d_y += (c[1]-center[1])**2
        d_z += (c[2]-center[2])**2

    distance = MATH.sqrt((d_x+d_y+d_z)/len(self.coordinates))

    self.properties = {
      "center": center,
      "size": size,
      "distance": distance,
    }
