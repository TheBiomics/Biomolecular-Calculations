
class Calculator:
  def __init__(self):
    pass


  def grid(self):
    PROCESS_DIR = self.config__docking.get("dir__base")

    DOCKING_DIR = HELP.validate_path(f"{PROCESS_DIR}/docking")

    HELP.log_info(DOCKING_DIR)

    RECEPTOR_PDBQT_DIR = f"{PROCESS_DIR}/mddaa-receptor-pdbqt"
    RECEPTOR_PDBQT_PATHS = list(PATH(RECEPTOR_PDBQT_DIR).glob('*.pdbqt'))


    with open(f"{PROCESS_DIR}/receptor-center-size.log","a+", encoding="utf-8") as f:
      f.writelines([
        "SERIAL    PDBQT    CENTER_X    CENTER_Y    CENTER_Z    SIZE_X    SIZE_Y    SIZE_Z\n",
      ])

    pdbqt_count = 0

    HELP.log_info(RECEPTOR_PDBQT_PATHS)
    for receptor_pdbqt in RECEPTOR_PDBQT_PATHS:
      pdbqt_count = pdbqt_count + 1
      filename_we = OS.path.basename(receptor_pdbqt)

      _array = OS.path.splitext(filename_we)
      filename = _array[-2]

      lines = []
      with open(receptor_pdbqt, 'r', encoding="utf8") as file:
          lines = file.readlines()

      protein_atom_hetatm = [x for x in lines if (x.startswith("HETATM") or x.startswith("ATOM"))]

      coordinates = []

      for atom_line in protein_atom_hetatm:
          _c_x = float(atom_line[31:38].strip())
          _c_y = float(atom_line[39:46].strip())
          _c_z = float(atom_line[47:54].strip())

          if not atom_line[13:14].startswith("H"):
              coordinates.extend([[_c_x, _c_y, _c_z]])

      props = HELP.get_grid_properties(coordinates)
      center_x = round(props['center'][0], 4)
      center_y = round(props['center'][1], 4)
      center_z = round(props['center'][2], 4)
      
      """
      Set Minimum than 126 as per AUTODOCK VINA's requirement
      """
      size_x = min(int(props['size'][0] + 10), 126)
      size_y = min(int(props['size'][1] + 10), 126)
      size_z = min(int(props['size'][2] + 10), 126)

      config_rec_file_content = f"""
receptor = {receptor_pdbqt}

center_x =  {center_x}
center_y =  {center_y}
center_z =  {center_z}

size_x = {size_x}
size_y = {size_y}
size_z = {size_z}

energy_range = 3
seed = 41103333
exhaustiveness = 16

"""
      with open(f"{PROCESS_DIR}/receptor-center-size.log","a+", encoding="utf-8") as f:
        f.writelines([
          f"{pdbqt_count}    {filename_we}    {center_x}    {center_y}    {center_z}    {size_x}    {size_y}    {size_z}\n",
        ])

      with open(f"{DOCKING_DIR}/{filename}.config.txt", "w+", encoding="utf-8") as f:
        f.writelines(config_rec_file_content)
    pass