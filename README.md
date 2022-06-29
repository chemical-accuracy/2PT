# 2PT
Two phase approximation (solid + gas) for performing thermodynamic calculations on liquids.
## History
The methodology was developed by Dr. Shiang-Tai Lin, Dr. Mario Blanco and Prof. William A. Goddard at the California Institute of Technology (Caltech).
It is published in [JCP 119, 11792 (2003)](https://doi.org/10.1063/1.1624057). Current version of the 2PT code is forked from [Tod A Pascal's repository](https://github.com/atlas-nano/2PT)
## Building the code
This describes how to build the code on most UNIX-based systems.
### Dependencies
1. C Compiler (e.g. g++, icpc etc.)
2. FFT3 library
The only non-standard dependency is the FFT3 library for the fourier transforms. It can be obtained [here](https://fftw.org/index.html).
However, at the moment the code is mostly set up to ineract with [LAMMPS](https://www.lammps.org/), so using LAMMPS output files is highly recommended.
### Quick start
`make -j 8 install` inside [2PT/2pt.v1.4/src](https://github.com/chemical-accuracy/2PT/tree/main/2pt.v1.4/src) usually works. 
This will create bin directory at the same level as the src directory with the executable.

If this does not work, you probably have to edit the [Makefile](https://github.com/chemical-accuracy/2PT/blob/main/2pt.v1.4/src/Makefile.gnu) to point to where your FFT3 library is located. Currently it points to the default installation location.

## Cite the 2PT method properly
If you are planning to use the 2PT method in your research, please cite the following seminal 2PT papers:
1. [JCP 119, 11792 (2003)](https://doi.org/10.1063/1.1624057) Original 2PT idea.
2. [JPCB 114(24), 8191 (2010)](https://pubs.acs.org/doi/full/10.1021/jp103120q) Extension to molecules
3. [PCCP 13, 169 (2011)](https://doi.org/10.1039/C0CP01549K) Validation of the method on many (~20) common solvents

