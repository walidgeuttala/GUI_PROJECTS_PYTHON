Dynamic Memory Allocation Simulation
This Python script provides a simple simulation of dynamic memory allocation using a graphical user interface (GUI) built with the Pygame library. The simulation focuses on three memory allocation algorithms: First Fit, Best Fit, and Worst Fit.

How to Use
Install Python and Pygame:
Before running the script, make sure you have Python installed. You can install Pygame by running the following command in your terminal or command prompt:

bash
Copy code
pip install pygame
Run the Script:
Execute the script by running it in your preferred Python environment. Upon running, the script will prompt you to enter the size of the memory (in megabytes), the number of programs to be simulated, and the memory allocation algorithm to use (1 for First Fit, 2 for Best Fit, 3 for Worst Fit).

Enter Program Details:
Once the initial setup is complete, you'll be prompted to enter details for each program, including the program name, size, and execution time.

Watch the Simulation:
The GUI window will display the memory layout and programs in different colors. The simulation will run, allocating and deallocating memory based on the chosen algorithm and program execution times.

Exit the Simulation:
To exit the simulation, simply close the GUI window. The script will print the final state of the memory allocation.

Code Overview
The script defines a class Mc representing the central memory, with methods for First Fit, Best Fit, and Worst Fit algorithms, as well as functions for GUI display and simulation control.

The Pygame library is used for creating a graphical representation of memory and programs.

The main function initializes the Pygame window, collects user input, creates an instance of the Mc class, and enters the main simulation loop.

Note: This script is designed for educational purposes to visually understand how different memory allocation algorithms work. It might not cover all edge cases or error handling for practical use.
