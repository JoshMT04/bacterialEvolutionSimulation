# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 21:53:09 2024

@author: joshm
"""

import numpy as np
import matplotlib.pyplot as plt

# Parameters
population_size = 5_000_000  # Number of individuals
generations = 10000  # Number of generations
mutation_rate = 1e-3  # Mutation rate per genome per generation
mutation_effect = -1  # Change in stability due to mutation
initial_stability = 10  # Initial protein stability
fitness_threshold = 2  # Minimum stability for survival
selection_weight = 0.8  # Selection pressure scale (0 = random, 1 = full stability-based)

# Initialize population stability
population = np.full(population_size, initial_stability, dtype=np.float32)

# Store average stability over generations
avg_stability = []

for generation in range(generations):
    # Apply mutations
    num_mutations = int(population_size * mutation_rate)
    mutation_indices = np.random.choice(population_size, num_mutations, replace=False)
    population[mutation_indices] += mutation_effect
    
    # Apply selection: Remove individuals below the fitness threshold
    population = population[population >= fitness_threshold]
    current_population_size = len(population)
    
    # Reproduce to maintain population size
    if current_population_size > 0:
        # Calculate fitness using selection weight
        baseline_fitness = 1  # Minimum fitness
        fitness = (baseline_fitness * (1 - selection_weight) + 
                   selection_weight * population)
        fitness /= np.sum(fitness)  # Normalize fitness
        
        # Generate the new population
        new_population = np.random.choice(
            population, size=population_size, p=fitness, replace=True
        )
        population = new_population
    
    # Track average stability
    avg_stability.append(np.mean(population))

# Plot average stability over generations
plt.plot(avg_stability)
plt.xlabel('Generation')
plt.ylabel('Average Stability')
plt.title(f'Evolution of Protein Stability (Selection Weight: {selection_weight})')
plt.savefig('/users/cohome/jm1622/ea_models/stability_evolution.png')
