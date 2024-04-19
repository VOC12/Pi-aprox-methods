# Parallel Pi Calculation Project

This project explores various methods for calculating the mathematical constant pi (π) using Python, focusing on both non-parallel and parallel programming techniques. The goal is to compare the efficiency and performance of different approaches when computing pi for different problem sizes.

## Overview

The project includes implementations of three different methods:

1. **Non-Parallel Calculation (`non_parallel.py`):**
   - Sequential computation of pi using mathematical formulas.
   - Efficient for smaller problem sizes but may become slower with larger inputs.

2. **Parallel Calculation with `multiprocessing` (`pi_by_multiprocessing.py`):**
   - Utilizes the `multiprocessing` module to distribute computation across multiple CPU cores.
   - Enables concurrent processing for improved performance on multi-core systems.

3. **Parallel Calculation with `mpi4py` (`pi_by_mpi4py.py`):**
   - Implements parallel computation using the `mpi4py` library for MPI-based distributed computing.
   - Scales well for larger problem sizes and distributed environments.

## File Structure

- `non_parallel.py`: Contains the non-parallel implementation of pi calculation.
- `pi_by_multiprocessing.py`: Implements pi calculation using the `multiprocessing` and Pool module.
- `pi_by_mpi4py.py`: Implements pi calculation using the `mpi4py` library for parallelism.
- `workers.py`: Contains helper functions/classes used in parallel implementations.
- `timemesure_analysis.ipynb`: Jupyter Notebook for performance analysis and comparison.

## Usage

1. **Non-Parallel Calculation:**
   ```bash
   python non_parallel.py

2. **Parallel Calculation with multiprocessing:**
   ```bash
   python pi_by_multiprocessing.py
   
3. **Parallel Calculation with mpi4py:**
   ```bash
   mpiexec -n <num_processes> python pi_by_mpi4py.py

## Requirements
Python 3.x
mpi4py (for pi_by_mpi4py.py)

## Report
For detailed insights and analysis, refer to the Parallel_Programming_with_Python_Report.pdf included in this repository.
