'''
The half-life of carbon-14 (C-14) is approximately 5,730 years. 
This means that if you start with a sample of C-14 atoms, after 5,730 years, 
half of the C-14 atoms in the sample will have decayed into stable 
nitrogen-14 (N-14) atoms.
Let's run it and see if we can confirm this fact.
'''

import random
import matplotlib.pyplot as plt

###################################################
# Set constants and init variables.
###################################################

# Constants for carbon-14 decay
# More initial atoms will give us more accuracy.
INITIAL_ATOMS_C14 = 1000  		# Initial number of C-14 atoms
DECAY_CONSTANT_C14 = 0.000121  	# Decay constant for C-14 (likeliness to decay per year)
TOTAL_YEARS = 7000  			# Total number of years to simulate

# This array will form the y-axis values
atoms_remaining_c14 = [INITIAL_ATOMS_C14]
# This array will form the x-axis values
years_elapsed = [0]

# We've now started with one point (0,INITIAL_ATOMS_C14)

###################################################
# Begin Monte Carlo simulation for C-14 decay
###################################################
for years in range(1, TOTAL_YEARS + 1):
    decayed_c14 = 0

	# atoms_remaining_c14[-1] is fancy shorthand for "the last element in the array"
	# We're looping through all remaining non-decayed atoms and giving them a chance
	# for the current year.
    for atom in range(atoms_remaining_c14[-1]):
        if random.uniform(0, 1) < DECAY_CONSTANT_C14:
            decayed_c14 += 1

	# Update count of total remaining atoms
    remaining_c14 = atoms_remaining_c14[-1] - decayed_c14

	# Append total remaining atom count to the y-values array.
    atoms_remaining_c14.append(remaining_c14)
	# Append the current year to the x-values array.
    years_elapsed.append(years)

###################################################
# Plot the results
###################################################
plt.figure(figsize=(10, 6))
plt.plot(years_elapsed, atoms_remaining_c14, label='Number of C-14 Atoms')
plt.xlabel('Years Elapsed')
plt.ylabel('Number of C-14 Atoms')
plt.title('Carbon-14 Radioactive Decay Simulation')
plt.legend()
plt.grid(True)
plt.show()

