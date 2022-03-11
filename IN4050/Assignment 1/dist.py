import numpy as np
import matplotlib.pyplot as plt
import math
import statistics
#import csv file
import csv
with open("european_cities.csv","r") as f:data=list(csv.reader(f, delimiter=';'))
cities=data[0]
distances=data[1:]

import itertools
import time
begin = time.time()

def distance_start_to_end(n, order):
    covered_distance = 0
    for i in range(0, n-1):
        start = order[i]
        end = order[i+1]
        covered_distance= covered_distance+float(distances[start][end])
    covered_distance= covered_distance+float(distances[order[n-1]][order[0]])
    return covered_distance

def exhaustive_search(n):
    tour = []
    best_distance=[]
    min_distance=0

    i = 0
    for i in range(0,n):
        tour.append(i)
    #List all the possiblities(permutations) of these cities
    options=list(itertools.permutations(tour,n))

    for o in options:
        covered_distance = distance_start_to_end(n, o)

        if min_distance == 0:
            min_distance = covered_distance
            best_order = o
        else:
            min_distance = covered_distance
            best_order = o

    print("Best tour: ", best_order)
    print("Route: ", [(cities[i]) for i in best_order])
    print("Minimal distance: ", min_distance)

# Find answer for 6 cities
exhaustive_search(6)
print("Time for running: %s seconds" % (time.time() - begin))


begin = time.time()
exhaustive_search(10)
print("Time for running: %s seconds" % (time.time() - begin))



time_per_loop=(15.43 *1000)/ math.factorial(10)

seconds= time_per_loop * math.factorial(24)

years= seconds/60/60/24/365

print(seconds) # time in seconds
print(years)  # time in years



#hill climbing

def index_mod(order, n):

    order=order.copy()
    # Choose two indexes randomly without replacement
    i,j=np.random.choice(list(range(0,n)),2,replace=False)
    # Swap their order
    order[i],order[j]=order[j], order[i]
    return order

def hill_climber(n):
    max = 1000
    # Start with a random order
    cities_order = np.arange(n)
    np.random.shuffle(cities_order)

    # Calculate distance of this order
    i = 0
    covered_distance = distance_start_to_end(n, cities_order)
    min_distance = covered_distance

    # Find some neighbours and compare the distance
    while i!=max:
        new_order = index_mod(cities_order,n)
        new_distance = distance_start_to_end(n, new_order)

        if(new_distance < min_distance):
            min_distance = new_distance
            cities_order = new_order
        i++

    return cities_order, min_distance


print("Best tour: ", hill_climber(10)[0])
print("Route: ", [(cities[i]) for i in hill_climber(10)[0]])
print("Minimal distance: ", hill_climber(10)[1])



# Here we run this hill climbing algorithm 20 times for both 10 cities and 24 cities
all_results_10_cities=[]
all_results_24_cities=[]

i = 0
while i!=20:
    all_results_10_cities.append(hill_climber(10)[1])
    all_results_24_cities.append(hill_climber(24)[1])
    i++

print("Best 20 runs: ", min(all_results_10_cities))
print("Worst 20 runs: ", max(all_results_10_cities))
print("Mean 20 runs: ", statistics.mean(all_results_10_cities))

#genetic algo
# Here we choose swap mutation and PMX as Crossover operator

# Swap Mutation
def swap_mutation(genotype):
    locuses = np.random.choice(len(genotype), 2, replace=False)
    genotype[locuses[0]], genotype[locuses[1]] = genotype[locuses[1]], genotype[locuses[0]]
    return genotype

# PMX
def pmx(a, b, start, stop):
    child = [None]*len(a)

    # Copy a slice from first parent:
    child[start:stop] = a[start:stop]

    # Map the same slice in parent b to child using indices from parent a:
    for ind, x in enumerate(b[start:stop]):
        ind = ind + start
        if x not in child:
            while child[ind] != None:
                ind = b.index(a[ind])
            child[ind] = x
    # Copy over the rest from parent b
    for ind, x in enumerate(child):
        if x == None:
            child[ind] = b[ind]

    return child

def pmx_pair(a, b):
    half = len(a) // 2
    start = np.random.randint(0, len(a)-half)
    stop = start+half
    return pmx(a, b, start, stop), pmx(b, a, start, stop)

def init_population(n, size):
    tour=np.arange(n)
    pop=[]
    if n < 10:
        pop=list(itertools.permutations(tour,n))
        np.random.shuffle(pop)
        return pop[0:size]
    else:
        i = 0
        for i in range(0,size):
            pop.append(np.random.permutation(tour))
        return pop

# Rank the population to select best individuals (shortest distance first)
def rank_selection(n, population):
    fitnessScore = [] # Fitness score as the route distance
    ranked_population = population.copy()
    for p in population:
        fitnessScore.append(distance_start_to_end(n, p))
    rank = np.argsort(fitnessScore)
    ranked_population = [ranked_population[i] for i in rank]
    return ranked_population

def genetic_algorithm(n, pop_size):
    # Initialize population
    pop = init_population(n, pop_size)
    parent_size = int(pop_size/2)
    best_fit=[]

    # Choose specified number of generations, for example, 50
    for i in range(0,50):
        offspring = []

        # Rank the population and select half of them with shorter distance
        parent_pop = rank_selection(n, pop)[0:parent_size]

        while p in parent_pop is not None:
            random_index = np.random.randint(0, parent_size, size=1)[0]
            offspring.append(swap_mutation(pmx_pair(list(p), list(parent_pop[random_index]))[0]))
            offspring.append(swap_mutation(pmx_pair(list(p), list(parent_pop[random_index]))[1]))

        # Survivor Selection: select from parents and offsprings and replace the old population
        new_pop = list(parent_pop) + list(offspring)
        pop= rank_selection(n, new_pop)[0:pop_size]

        best_fit.append(distance_start_to_end(n,pop[0]))

    distance=[]
    for p in pop:
        distance.append(distance_start_to_end(n,p))
    return distance[0], best_fit


# Define three different values for population size
popSize1=10
popSize2=50
popSize3=100

# Here we run this GA algorithm 20 times for both 10 cities and 24 cities
all_results_10_cities_pop1=[]
all_results_10_cities_pop2=[]
all_results_10_cities_pop3=[]


i = 0
for i in range(20):
    all_results_10_cities_pop1.append(genetic_algorithm(10, popSize1)[0])
    all_results_10_cities_pop2.append(genetic_algorithm(10, popSize2)[0])
    all_results_10_cities_pop3.append(genetic_algorithm(10, popSize3)[0])

print("-------------10 cities with population size 10------------------")
print("Best of 20 runs: ", min(all_results_10_cities_pop1))
print("Worst of 20 runs: ", max(all_results_10_cities_pop1))
print("Mean of 20 runs: ", statistics.mean(all_results_10_cities_pop1))
print("Sandard deviation of 20 runs: ", statistics.stdev(all_results_10_cities_pop1))





for a in [10,24]:
    for b in [10,50,100]:
        plt.plot(np.arange(50), genetic_algorithm(a,b)[1])
        plt.ylabel('Generation')
        plt.ylabel('Distance') # Here I choose distance as fitness value, shortest is the best
    plt.show()




# Running time with poplation 100
begin = time.time()
genetic_algorithm(10, popSize3)
print("Time for running: %s seconds" % (time.time() - begin))
begin = time.time()
genetic_algorithm(24, popSize3)
print("Time for running: %s seconds" % (time.time() - begin))



# Lamarckian

# It should better if I write the original function properly. Here I just rewrite the function.
def new_hill_climber(initial):
    max = 1000
    # Calculate distance of this order
    i = 0
    covered_distance = distance_start_to_end(len(initial), initial)
    min_distance = covered_distance

    # Find some neighbours and compare the distance
    while i in range(max):
        new_order = index_mod(initial,len(initial))
        new_distance = distance_start_to_end(len(initial), new_order)

        if(new_distance < min_distance):
            min_distance = new_distance
            initial = new_order

    return initial, min_distance

def new_genetic_algorithm(n, pop_size):
    # Initialize population
    pop = init_population(n, pop_size)
    parent_size = int(pop_size/2)
    best_fit=[]

    # Choose specified number of generations, for example, 50
    for i in range(0,50):
        offspring = []

        # Rank the population and select half of them with shorter distance
        parent_pop = rank_selection(n, pop)[0:parent_size]

        for p in parent_pop:
            random_index = np.random.randint(0, parent_size, size=1)[0]
            offspring.append(swap_mutation(pmx_pair(list(p), list(parent_pop[random_index]))[0]))
            offspring.append(swap_mutation(pmx_pair(list(p), list(parent_pop[random_index]))[1]))

        if i < 1:
            new_offspring = []
            for q in offspring:
                new_offspring.append(new_hill_climber(list(q))[0])
        else: new_offspring = offspring.copy()

        # Survivor Selection: select from parents and offsprings and replace the old population
        new_pop = list(parent_pop) + list(new_offspring)
        pop= rank_selection(n, new_pop)[0:pop_size]

        best_fit.append(distance_start_to_end(n,pop[0]))

    distance=[]
    for p in pop:
        distance.append(distance_start_to_end(n,p))
    return distance[0], best_fit


# Define three different values for population size
popSize1=10
popSize2=50
popSize3=100

# Here we run this GA algorithm 20 times for both 10 cities and 24 cities
all_results_10_cities_pop1=[]
all_results_10_cities_pop2=[]
all_results_10_cities_pop3=[]

i = 0
while i!=20:
    all_results_10_cities_pop1.append(new_genetic_algorithm(10, popSize1)[0])
    all_results_10_cities_pop2.append(new_genetic_algorithm(10, popSize2)[0])
    all_results_10_cities_pop3.append(new_genetic_algorithm(10, popSize3)[0])
    i++


print("-------------10 cities------------------")
print("Population size:",popSize1,"\nBest of 20 runs: ", min(all_results_10_cities_pop1),
      "Worst of 20 runs: ", max(all_results_10_cities_pop1),
      "Mean of 20 runs: ", statistics.mean(all_results_10_cities_pop1),
      "Sandard deviation of 20 runs: ", statistics.stdev(all_results_10_cities_pop1))


# Lamarckian
for a in [10,24]:
    for b in [10,50,100]:
        plt.plot(np.arange(50), new_genetic_algorithm(a,b)[1])
        plt.ylabel('generation')
        plt.ylabel('fitness(=distance:minimum is the best)')
    plt.show()



# Balwinian: Do not replace the original poplulation, only improve fitness.
# Here I change the fitness to hill climber method and then set into the GA algorithm.

def fitness(data):
    fit=new_hill_climber(data)[1]
    return fit

def new_rank_selection(n, population):
    fitnessScore = [] # Fitness score as the route distance
    ranked_population = population.copy()
    for p in population:
        fitnessScore.append(fitness(p))
    rank = np.argsort(fitnessScore)
    ranked_population = [ranked_population[i] for i in rank]
    return ranked_population

def bal_genetic_algorithm(n, pop_size):
    # Initialize population
    pop = init_population(n, pop_size)
    parent_size = int(pop_size/2)
    best_fit=[]

    # Choose specified number of generations, for example, 50
    for i in range(0,50):
        offspring = []

        # Rank the population and select half of them with shorter distance
        if i < 3:
            parent_pop = new_rank_selection(n, pop)[0:parent_size]
        else:
            parent_pop = rank_selection(n, pop)[0:parent_size]

        for p in parent_pop:
            random_index = np.random.randint(0, parent_size, size=1)[0]
            offspring.append(swap_mutation(pmx_pair(list(p), list(parent_pop[random_index]))[0]))
            offspring.append(swap_mutation(pmx_pair(list(p), list(parent_pop[random_index]))[1]))

        # Survivor Selection: select from parents and offsprings and replace the old population
        new_pop = list(parent_pop) + list(offspring)
        pop= rank_selection(n, new_pop)[0:pop_size]

        best_fit.append(distance_start_to_end(n,pop[0]))

    distance=[]
    for p in pop:
        distance.append(distance_start_to_end(n,p))
    return distance[0], best_fit


# Here we run this GA algorithm 20 times for both 10 cities and 24 cities
all_results_10_cities_pop1=[]
all_results_10_cities_pop2=[]
all_results_10_cities_pop3=[]


i = 0
while i!=20:
    all_results_10_cities_pop1.append(bal_genetic_algorithm(10, popSize1)[0])
    all_results_10_cities_pop2.append(bal_genetic_algorithm(10, popSize2)[0])
    all_results_10_cities_pop3.append(bal_genetic_algorithm(10, popSize3)[0])
    i++


print("Population size:",popSize1,"\nBest of 20 runs: ", min(all_results_10_cities_pop1),
      "Worst of 20 runs: ", max(all_results_10_cities_pop1),
      "Mean of 20 runs: ", statistics.mean(all_results_10_cities_pop1),

# Balwinian
for a in [10,24]:
    for b in [10,50,100]:
        plt.plot(np.arange(50), bal_genetic_algorithm(a,b)[1])
        plt.ylabel('generation')
        plt.ylabel('fitness(=distance:minimum is the best)')
    plt.show()


