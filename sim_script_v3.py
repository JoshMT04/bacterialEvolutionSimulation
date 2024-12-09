from sim_functions import *

pop_size = 500000
gens = 1500
mutate_rate = 1e-3
init_stability = 25
crit_stability = 0
poi_bases = 9159
population = np.full(pop_size, init_stability, dtype=np.float32)

# runs  = ['marginal', 'two_peaks', 'neutral']
# for i in runs:
#     full_sim(population, pop_size, gens, mutate_rate, poi_bases, crit_stability, i, 20)

full_sim(population, pop_size, gens, mutate_rate, poi_bases, crit_stability, 'two_peaks', 10)