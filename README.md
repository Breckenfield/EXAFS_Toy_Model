# EXAFS_Toy_Model
Python code to simulate the output of an EXAFS Experiment

MultiScatter.py is run and reads from Material.json for experimental information. Functions.py is what it says on the tin.

To run MultiScatter.py you will need Material.json and Functions.py in the same folder.

-Materials and how to use them
-

The materials are stored in a .json format

e.g.
'''''''
"Copper":{
		"Symbol":"Cu",
		"RadiusDistance": [2.2, 3.3, 4.1, 4.7, 5.3, 5.8],
		"NumberOfAtoms": [12, 6, 24, 32, 12, 8],
		"Temperature": 300,
		"AtomicMass": [63.546, 63.546, 63.546, 63.546, 63.546, 63.546],
		"EinsteinTemperature": [343.5, 343.5, 343.5, 343.5, 343.5, 343.5]
	},
'''''''

Radius Distance, Number Of Atoms, Atomic Mass and Einstein Temperature all need to be the SAME length. 
You can set the Atomic Mass and Einstein Tempurature per Radius for materials with multiple elements.

