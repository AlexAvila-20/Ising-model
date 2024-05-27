import numpy as np
import matplotlib.pyplot as plt
import random
import copy
import os
from scipy.ndimage import convolve, generate_binary_structure
from matplotlib.colors import ListedColormap

yellow = '#FFFF00'
purple = '#2E0854'
colours = ListedColormap(['yellow', 'purple'])
folder_name = "Plots"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

#Grid
N = 20
total_steps = 100000

lattice_spins = np.random.choice([-1, 1], size = (N, N))
initial_configuration = copy.deepcopy(lattice_spins)


def get_energy(lattice):
  kern = generate_binary_structure(2,1)
  kern[1][1] = False
  arr = -lattice * convolve(lattice, kern, mode='constant', cval=0)
  return arr.sum()

def get_magnetization(lattice):
  return lattice.sum()

#Temperature list:
temperatures = np.linspace(0.1, 10, 200)
boltzmann_constant = 1

#Creating empty lists to store the average energies, heat capacities, average magnetizations, and susceptibility of magnetization:
avg_energies = [] #List of average energies for each T.
heat_capacities = [] #List of average heat capacities for each T.
avg_magnetization = [] #List of average magnetizations for each T.
magnetization_susceptibilities = [] #List of average magnetic susceptibilities for each T.
for T in temperatures:
    #Monte Carlo energies for this temperature:
    energies = []
    #Monte Carlo magnetizations for this temperature:
    magnetizations = []
    for step in range(total_steps):
        #Select a random spin:
        i, j = random.randint(0, N-1), random.randint(0, N-1)
        #Calculate the energy of the current state:
        energy = get_energy(lattice_spins)
        #Calculate the magnetization of the current state:
        magnetization = get_magnetization(lattice_spins)
        #Changing the spin:
        lattice_spins[i, j] *= -1
        #Calculate the energy of the new state:
        new_energy = get_energy(lattice_spins)
        #Calculate magnetization of the new state:
        new_magnetization = get_magnetization(lattice_spins)
        #Calculate the energy difference:
        deltaE = new_energy - energy
        #Accept or reject the change with the appropriate probability based on the Metropolis criterion:
        if deltaE <= 0 or np.exp(-deltaE /(boltzmann_constant * T)) > random.uniform(0, 1):
            energies.append(new_energy)
            magnetizations.append(new_magnetization)
        else:
            #Revert the change:
            lattice_spins[i, j] *= -1
            energies.append(energy)
            magnetizations.append(magnetization)
        #Average energy for this temperature:
    avg_energies.append(2*np.mean(energies)/N**2)
    #Average magnetization for this temperature:
    avg_magnetization.append(np.mean(magnetizations)/N**2)
    sqrt_energies = [ener**2 for ener in energies] #The square of the energies.
    Energyprom = np.mean(energies) #<E> for this T.
    EnergySprom = np.mean(sqrt_energies) #<E^2> for this T.
    #Average heat capacity for this temperature:
    heat_capacities.append((EnergySprom-Energyprom**2)/(N**2*boltzmann_constant*T**2))
    sqrt_magnetizations = [magnets**2 for magnets in magnetizations] #Square of the magnetizations.
    AbsMag = [abs(magnet) for magnet in magnetizations] #Absolute value of the magnetizations.
    Magnetprom = np.mean(AbsMag) #<|M|>
    MagnetSprom = np.mean(sqrt_magnetizations) #<M^2>
    #Average magnetic susceptibility for this temperature:
    magnetization_susceptibilities.append((MagnetSprom-Magnetprom**2)/(N**2*boltzmann_constant*T))

    print("for T= ", T, " Expected energy = ", 2*np.mean(energies)/N**2, " Expected magnetization = ", np.mean(magnetizations)/N**2 , " Average heat capacity = ", (EnergySprom-Energyprom**2)/(N**2*boltzmann_constant*T**2), "Average magnetic susceptibility = ", (MagnetSprom-Magnetprom**2)/(N**2*boltzmann_constant*T))
heat_capacities[0]=0 #In order to obtain a correct graph, we replace the first value of heatcap since it is very large.
magnetization_susceptibilities[0]=0 #Likewise the susceptibility.
final_configuration=copy.deepcopy(lattice_spins) #Making a copy of the final configuration.

#Plots
plt.matshow(initial_configuration, cmap=colours)
plt.title('Initial configuration')
plt.savefig(os.path.join(folder_name, "initial_configuration.png"))
plt.close()

plt.matshow(final_configuration, cmap=colours)
plt.title('Final configuration')
plt.savefig(os.path.join(folder_name, "final_configuration.png"))
plt.close()


plt.scatter(temperatures, heat_capacities, color="blue", s=10)
plt.xlabel('Temperature')
plt.ylabel('Average Heat Capacity (<C>)')
plt.title('Average Heat Capacity vs. Temperature')
plt.savefig(os.path.join(folder_name, "heat_capacity_vs_temperature.png"))
plt.close()


plt.scatter(temperatures, avg_energies, color="blue", s=10)
plt.xlabel('Temperature')
plt.ylabel('Expected Energy (<E>)')
plt.title('Expected Energy vs Temperature')
plt.savefig(os.path.join(folder_name, "energy_vs_temperature.png"))
plt.close()

plt.scatter(temperatures, avg_magnetization, color="blue", s=10)
plt.xlabel('Temperature')
plt.ylabel('Expected Magnetization (<M>)')
plt.title('Expected  Magnetization vs Temperature')
plt.savefig(os.path.join(folder_name, "magnetization_vs_temperature.png"))
plt.close()

plt.scatter(temperatures, magnetization_susceptibilities, color="blue", s=10)
plt.xlabel('Temperature')
plt.ylabel('Magnetic Susceptibility')
plt.title('Magnetic Susceptibility vs Temperature')
plt.savefig(os.path.join(folder_name, "magnetic_susceptibility_vs_temperature.png"))
plt.close()
