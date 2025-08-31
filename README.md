

# Bee Simulation project - Taking Care Of Beezness
- COMP1005 Assignment

#Student Name: Layla Dawood
#Student ID: 23100624


#Description of the program:

This program simulates the behavior of honey bees in a 2D environment. Bees leave the hive, collect nectar from flowers and return to store honey. This simulation includes a visual representation of bee positions, flower status, hive location and a honeycomb frame that fills as bees deliver the nectar.

The simulation supports both interactive and batch input modes. Parameters such as the number of bees and simulation length can be controlled via user input or a parameter file.



#Files Included:

- beeworld.py – Main simulation script
- buzzness.py – Class definitions for Bee, Flower, and Frame
- params.csv – Sample batch parameter file
- README.txt – This file
- Project_Report_23100624.docx – Project report 



#Requirements

- Python 3
- Required libraries:
  - matplotlib
  - csv
  - argparse
- (Optional) numpy if extended

If graph window does not show,  use the correct backend with:
python
matplotlib.use('TkAgg')
