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

Instructions for running source code (on Windows):
1)	First, download the folder titled idealbrakecurve attached, which contains the source code.

2)	Open/Download VSCode (for Windows) which is the IDE used to run the code:
VSCode Download Link: https://code.visualstudio.com/download

3)	To download Python, version: python 3.9.6, follow the following link:
https://www.python.org/downloads/release/python-396/
•	Download the Windows installer (64-bit) from the bottom of that page. During installation, tick “Add Python 3.9 to PATH” before clicking Install.
•	Use python --version to show the version of the installation, which should be 3.9.6 as that is the version the code was written and tested in.
•	If python points to another version, then py -3.9 should be substituted for python in step 5. After that python can be used as you are now working within the virtual environment.

4)	Then open Command Prompt or PowerShell (or the VSCode terminal) and ensure that you are in the correct working directory i.e: the directory of the folder containing the source code:
•	The working directory can be checked using cd (Command Prompt) or pwd (PowerShell).
•	Using the command dir (Command Prompt) or ls (PowerShell) you should see the file idealBrakeCurve.py listed.
•	If in the wrong directory, use cd followed by your directory path to enter the correct directory. If the folder is on a different drive, switch drive first, e.g. D:.

5)	Create a virtual environment within the folder:
(Command Prompt):
python -m venv .venv
.venv\Scripts\activate.bat
(PowerShell):
python -m venv .venv
.venv\Scripts\Activate.ps1
•	If PowerShell blocks the activation script with an error about execution policies, run Set-ExecutionPolicy -Scope CurrentUser RemoteSigned, confirm, and try again (or use Command Prompt instead).
•	A virtual environment is used to install libraries like Matplotlib & NumPy in so that each project’s downloaded libraries are isolated on your device. This prevents conflicts between different versions of the same libraries, which would otherwise occur if they were saved in a shared location.
•	After running the above commands, you know if it has worked and the environment is active if the terminal prompt starts with (.venv).

6)	Download Matplotlib & NumPy:
pip install numpy matplotlib

7)	Then enter the following into the terminal:
python idealBrakeCurve.py

8)	On later runs repeat Step 4, run .venv\Scripts\activate.bat (Command Prompt) or .venv\Scripts\Activate.ps1 (PowerShell) and repeat Step 7.

Instructions for running source code (on Linux):

1)	First, download the folder titled idealbrakecurve attached, which contains the source code.

2)	Open/Download VSCode (for Linux) which is the IDE used to run the code:
VSCode Download Link: https://code.visualstudio.com/download
•	Choose the .deb package (Debian/Ubuntu) or .rpm package (Fedora/RHEL), or install it through your distribution’s software centre or Snap.

3)	To download Python, version: python 3.9.6, follow the following link:
https://www.python.org/downloads/release/python-396/

•	On Linux, Python is usually installed through your package manager or built from the source tarball on that page. For example, on Debian/Ubuntu, you may need sudo apt install python3.9 python3.9-venv python3-pip (if 3.9 isn’t available in your default repositories, build from source or use a tool such as pyenv).
•	Use python3 --version to show the version of the installation, which should be 3.9.6 as that is the version the code was written and tested in.
•	If python3 points to another version, then python3.9 should be substituted for python3 in step 5, after that python3 can be used as you are now working within the virtual environment.

4)	Then open the terminal and ensure that you are in the correct working directory i.e: the directory of the folder containing the source code:

•	The working directory can be checked using pwd.
•	Using the command ls you should see the file idealBrakeCurve.py listed.
•	If in the wrong directory, use cd followed by your directory path to enter the correct directory.

5)	Create a virtual environment within the folder:
python3 -m venv .venv
source .venv/bin/activate

•	A virtual environment is used to install libraries like Matplotlib & NumPy in so that each project’s downloaded libraries are isolated on your device. This prevents conflicts between different versions of the same libraries, which would otherwise occur if they were saved in a shared location.
•	After running the above commands, you know if it has worked and the environment is active if the terminal prompt starts with (.venv).
•	If you get an error saying the venv module or ensurepip is missing, install it first, e.g. sudo apt install python3.9-venv on Debian/Ubuntu.

6)	Download Matplotlib & NumPy:
pip3 install numpy matplotlib
•	If the plot window doesn’t open, Matplotlib may need a GUI backend. On Debian/Ubuntu, sudo apt install python3-tk usually fixes this.

7)	Then enter the following into the terminal:
python3 idealBrakeCurve.py

8)	On later runs repeat Step 4, run source .venv/bin/activate and repeat Step 7
