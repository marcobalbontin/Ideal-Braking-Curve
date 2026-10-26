# Ideal-Braking-Curve
Instructions for running source code (on Mac):
1)	First, download the folder titled idealbrakecurve attached, which contains the source code.

2)	Open/Download VSCode (for MacOS) which is the IDE used to run the code:
	VSCode Download Link: https://code.visualstudio.com/download 

3)	To download Python, version: python 3.9.6, follow the following link:
https://www.python.org/downloads/release/python-396/ 
-	Use python3 --version to show the version of the installation, which should be 3.9.6 as that is the version the code was written and tested in.
-	If python3 points to another version, then python3.9 should be substituted for python3 in step 5. After that python3 can be used as you are now working within the virtual environment.

4)	Then open the terminal and ensure that you are in the correct working directory i.e: the directory of the folder containing the source code:
-	The working directory can be checked using pwd
-	Using the command ls you should see the file idealBrakeCurve.py listed.
-	If in the wrong directory, use cd directory path to enter the correct directory.

5)	Create a virtual environment within the folder:
	python3 -m venv .venv
	source .venv/bin/activate
-	A virtual environment is used to install libraries like Matplotlib & NumPy in so that each project's downloaded libraries are isolated on your device. This prevents conflicts between different versions of the same libraries, which would otherwise occur if they were saved in a shared location.
-	After running the above commands, you know if it has worked and the environment is active if the terminal prompts start with (.venv)

6)	Download Matplotlib & NumPy:
pip3 install numpy matplotlib

7)	Then enter the following into the terminal:
python3 idealBrakeCurve.py
8)	On later runs repeat Step 4, run source .venv/bin/activate and repeat Step 7.

