# EXAFS_Toy_Model

Python code to simulate the output of an EXAFS Experiment

multiscatter.py is run and reads from Material.json for material information.

To run multiscatter.py you will need Material.json and functions.py in the same folder

Materials and how to use them
-

- The materials are stored in a .json format
- The user can pick the material they want to use from Material.json
- Radius Distance, Number Of Atoms, Atomic Mass and Einstein Temperature all need to be the <b>SAME</b> length.
- <b>"RadiusDistance"</b> is the distance from the "center" atom measured in angstroms
- <b>"NumberOfAtoms"</b> is the number of atoms of of the element at that radius
- <b>"Tempurature"</b> is the tempurature of the material in kelvin
- <b>"AtomicMass"</b> is the atomic mass of the element at that radius
- <b>"EinsteinTempurature"</b> is the specific Einstein Tempurature of the element at that radius in kelvin

e.g.

<pre><code>
"Copper":{
	"Symbol":"Cu",
	"RadiusDistance": [2.2, 3.3, 4.1, 4.7, 5.3, 5.8],
	"NumberOfAtoms": [12, 6, 24, 32, 12, 8],
	"Temperature": 300,
	"AtomicMass": [63.546, 63.546, 63.546, 63.546, 63.546, 63.546],
	"EinsteinTemperature": [343.5, 343.5, 343.5, 343.5, 343.5, 343.5]	
	}
</code></pre>
- You can set the Atomic Mass and Einstein Tempurature per Radius for materials with multiple elements.

e.g.

<pre><code>
"Multiple Element Example":{
	"Symbol":"Iron and Carbon mixed",
	"RadiusDistance": [0.9, 1.95, 1.95, 2.4, 4.1, 6],
	"NumberOfAtoms": [6, 32, 64, 8, 12, 6],
	"Temperature": 300,
	"AtomicMass": [55.845, 12, 55.845, 12, 55.845, 55.845],
	"EinsteinTemperature": [470, 2230, 470, 2230, 470, 470]
	}
</code></pre>

