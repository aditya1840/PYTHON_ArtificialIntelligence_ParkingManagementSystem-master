# PYTHON_ArtificialIntelligence_ParkingProblem
AI search techniques using "Python".  
This code demonstrates a search algorithm using various search methods (DFS, BFS, Best-First Search) to solve a parking problem. 
It explores different paths to find the optimal sequence of moves that allows cars to enter the parking lot efficiently.  
The code times the execution and outputs the duration it takes to find the solution.

A final project in Python for the subject "Artificial Intelligence" at University of West Attica 2020-21. 
<p align="center">
<img src="https://github.com/PaolaVlsc/PYTHON_ArtificialIntelligence_ParkingManagementSystem/assets/87998374/238d7403-3fd3-451d-a6ab-06ec644f63f5" alt="initial" width="20%">
</p>


# ParkingFourSpaces

## Description
The program simulates parking spaces and vehicles in a parking lot. 
* It explores different paths to find the optimal sequence of moves that allows cars to enter the parking lot efficiently. 
* The code uses a recursive approach to create a search tree and tracks the states of the system until a solution is found. 
* The search is performed on the parking problem, and the results are printed to the console. 

There are three different versions of the solution provided.
1. Four spaces  - ParkingFourSpaces.py
2. Extended to six spaces - Extended_ParkingSixSpaces.py
3. Extended to nine spaces - Extended_ParkingNineSpaces.py

## Table of Contents
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Methods](#methods)
- [Contributors](#contributors)
- [Extras](#extras)

## Prerequisites
- Python (3.x recommended)

## Usage
1. Clone this repository to your local machine.
2. Run the `ParkingFourSpaces.py` file using Python.
3. Select your desired search method (DFS, BFS, or BestFS) in the `method` variable in the `main()` function.

Example:
```python
method = 'BestFS'
```

## Methods
This program supports three search methods for solving the parking puzzle:

1. **Depth-First Search (DFS):** To use this method, set the `method` variable in the `main()` function to `'DFS'`.

2. **Breadth-First Search (BFS):** To use this method, set the `method` variable in the `main()` function to `'BFS'`.

3. **Best-First Search (BestFS):** To use this method, set the `method` variable in the `main()` function to `'BestFS'`.

You can choose your desired search method by modifying the `method` variable as described above.

## Contributors
This project was created by:
- Velasco Paola
- Micha Evagelia 

## Extras
* Report paper in greek: [Report paper](https://github.com/PaolaVlsc/PYTHON_ArtificialIntelligence_ParkingProblem/blob/master/extra/Final_Parking_cs161020_cs171102.pdf)
