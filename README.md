# Monte Carlo Simulation of Ising Model

This repository contains a Python script for simulating the Ising model using the Metropolis-Hastings algorithm. The script calculates various thermodynamic properties of the system, such as energy, magnetization, heat capacity, and magnetic susceptibility, as functions of temperature.

## Requirements

To run the script, you need the following Python libraries:
- numpy
- matplotlib
- scipy

You can install these libraries using pip:

```
pip install numpy matplotlib scipy
```

#Usage

Run the script to perform the Monte Carlo simulation and generate plots. The script saves the plots in a folder named Plots.

```
python ising_model_simulation.py
```

Description

The script performs the following steps:

1. Initializes a 20x20 lattice with random spins (-1 or 1).
2. Defines functions to calculate the energy and magnetization of the lattice.
3. Iterates over a range of temperatures to perform the Metropolis-Hastings algorithm:
  * Selects a random spin.
  * Calculates the energy and magnetization of the current state.
  * Flips the selected spin and calculates the new energy and magnetization.
  * Accepts or rejects the new state based on the Metropolis criterion.
  * Records the energy and magnetization for each step.
4. Calculates average energies, heat capacities, average magnetizations, and magnetic susceptibilities for each temperature.
5. Generates and saves the following plots:
  * Initial and final spin configurations.
  * Average heat capacity vs. temperature.
  * Expected energy vs. temperature.
  * Expected magnetization vs. temperature.
  * Magnetic susceptibility vs. temperature.

# Plots

The following plots are generated and saved in the Plots folder:

* initial_configuration.png: Initial spin configuration.
* final_configuration.png: Final spin configuration after the simulation.
* heat_capacity_vs_temperature.png: Average heat capacity vs. temperature.
* energy_vs_temperature.png: Expected energy vs. temperature.
* magnetization_vs_temperature.png: Expected magnetization vs. temperature.
* magnetic_susceptibility_vs_temperature.png: Magnetic susceptibility vs. temperature.
