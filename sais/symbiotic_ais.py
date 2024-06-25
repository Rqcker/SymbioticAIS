import time
import numpy as np

from .benchmarks import bound, benchmark_result, terminate

__all__ = ['run']


def run(population_size, benchmark_number):
    """
    Execute the SAIS algorithm for a given benchmark and population size.

    Args:
        population_size (int): The total number of solutions to generate.
        benchmark_number (int): The identifier for the benchmark test.

    Returns:
        tuple: Contains the best solution found, its fitness, total run time,
               total iterations, and iteration results.
    """
    print(
        f"Starting SAIS for benchmark {benchmark_number} "
        f"with population size {population_size}."
    )
    start_time = time.time()
    # initialize the SAIS algorithm 3 core parts size
    symbiotic_population_size = int(population_size / 3)

    # initialize the population of solutions
    population = []
    (global_min, lower_bound, upper_bound,
        nd, max_limit) = terminate(benchmark_number)
    for i in range(population_size):
        x = np.random.uniform(lower_bound, upper_bound, nd)
        y = benchmark_result(x, benchmark_number)
        solution = (x, y)
        population.append(solution)

    # iterate through the Symbiotic AIS optimization process
    iterations_number = 0
    iteration_results = []
    while iterations_number < max_limit:
        # initialize memory_population (clone)
        memory_population = population.copy()

        # initialize Mutualism, Commensalism and Parasitism populations
        mutualism_population = population[:symbiotic_population_size]
        commensalism_population = \
            population[symbiotic_population_size:2*symbiotic_population_size]
        parasitism_population = \
            population[2*symbiotic_population_size:3*symbiotic_population_size]

        # removing 3 parts from the population
        for part in [mutualism_population, commensalism_population,
                     parasitism_population]:
            for item in part:
                if item in population:
                    population.remove(item)

        # mutualism group start
        # update the best antibodies mutualism_population
        sorted_indices_mu = np.argsort([i[1] for i in mutualism_population])
        # pre-extracted index slices
        selected_indices_mu = sorted_indices_mu[:symbiotic_population_size]
        best_antibodies_mu = [
            mutualism_population[j][0] for j in selected_indices_mu
        ]
        best_fitness_list_mu = [
            mutualism_population[j][1] for j in selected_indices_mu
        ]

        # select the best one
        # best_fitness is my breakpoint test
        best_fitness_mu, idx_mu = \
            min((v, i) for i, v in enumerate(best_fitness_list_mu))
        best_antibody_mu = best_antibodies_mu[idx_mu]

        # define the benefit factor 1 or 2
        bf = np.random.randint(1, 3, size=nd)

        # update best antibodies
        for j in range(symbiotic_population_size):
            i = np.random.randint(0, symbiotic_population_size)
            if i == j:
                i = np.random.randint(0, symbiotic_population_size)
            # define mutual factor
            mu = (best_antibodies_mu[i] + best_antibodies_mu[j]) / 2
            # get previous fitness for comparison
            old_fitness_i = \
                benchmark_result(best_antibodies_mu[i], benchmark_number)
            old_fitness_j = \
                benchmark_result(best_antibodies_mu[j], benchmark_number)
            # calculate new solution
            new_antibody_i = best_antibodies_mu[i] + \
                np.random.uniform(0, 1, nd) * (best_antibody_mu - mu*bf)
            new_antibody_i = bound(new_antibody_i, upper_bound, lower_bound)
            new_antibody_j = best_antibodies_mu[j] + \
                np.random.uniform(0, 1, nd) * (best_antibody_mu - mu*bf)
            new_antibody_j = bound(new_antibody_j, upper_bound, lower_bound)
            # evaluate the fitness of the new solution
            new_fitness_i = benchmark_result(new_antibody_i, benchmark_number)
            new_fitness_j = benchmark_result(new_antibody_j, benchmark_number)
            # comparison:
            if new_fitness_i < old_fitness_i:
                # replace old antibody and fitness with new ones
                population.append((new_antibody_i, new_fitness_i))
            elif new_fitness_i >= old_fitness_i:
                population.append((best_antibodies_mu[i], old_fitness_i))
            elif new_fitness_j < old_fitness_j:
                # replace old antibody and fitness with new ones
                population.append((new_antibody_j, new_fitness_j))
            elif new_fitness_j >= old_fitness_j:
                population.append((best_antibodies_mu[j], old_fitness_j))

        # mutualism group end

        # commensalism group start
        # update the best antibodies commensalism_population
        sorted_indices_co = np.argsort([i[1] for i in commensalism_population])
        # pre-extracted index slices
        selected_indices_co = sorted_indices_co[:symbiotic_population_size]
        best_antibodies_co = [
            commensalism_population[j][0] for j in selected_indices_co
        ]
        best_fitness_list_co = [
            commensalism_population[j][1] for j in selected_indices_co
        ]

        # select the best one
        # best_fitness is my breakpoint test
        best_fitness_co, idx_co = \
            min((v, i) for i, v in enumerate(best_fitness_list_co))
        best_antibody_co = best_antibodies_co[idx_co]

        # update best antibodies
        for j in range(symbiotic_population_size):
            i = np.random.randint(0, symbiotic_population_size)
            if i == j:
                i = np.random.randint(0, symbiotic_population_size)
            # get previous fitness for comparison
            old_fitness_co = \
                benchmark_result(best_antibodies_co[j], benchmark_number)
            # calculate new solution
            new_antibody_co = best_antibodies_co[j] + \
                np.random.uniform(-1, 1, nd) * \
                (best_antibody_co - best_antibodies_co[i])
            new_antibody_co = bound(new_antibody_co, upper_bound, lower_bound)
            # evaluate the fitness of the new solution
            new_fitness_co = \
                benchmark_result(new_antibody_co, benchmark_number)
            # comparison:
            if new_fitness_co < old_fitness_co:
                # replace old antibody and fitness with new ones
                population.append((new_antibody_co, new_fitness_co))
            else:
                population.append((best_antibodies_co[j], old_fitness_co))

        # commensalism group end

        # parasitism group start
        for idx in range(len(parasitism_population)):
            parasite_solution = np.random.uniform(lower_bound, upper_bound, nd)
            parasite_fitness = \
                benchmark_result(parasite_solution, benchmark_number)
            host_index = np.random.randint(0, len(parasitism_population))
            if host_index == idx:
                host_index = np.random.randint(0, len(parasitism_population))
            host_fitness = parasitism_population[host_index][1]
            if parasite_fitness < host_fitness:
                parasitism_population[host_index] = \
                    (parasite_solution, parasite_fitness)

        population = population + parasitism_population
        # parasitism group end
        population = population + memory_population

        # update the best antibodies population quick way :)
        best_solution = min(population, key=lambda x: x[1])
        best_fitness = best_solution[1]
        best_antibody_part = best_solution[0]
        # store iteration data as dict
        iteration_data = {
            'Iteration': iterations_number,
            'BestFitness': best_fitness,
            'BestAntibody': best_antibody_part
        }
        iteration_results.append(iteration_data)
        # sorted popualtion which with double size
        population = sorted(population, key=lambda x: x[1])
        half_size = len(population) // 2
        # make sure same size as old population and get top antibodies
        population = population[:half_size]
        # check if termination conditions are met
        if best_fitness < global_min:
            print('Iterations Number:', iterations_number)
            break
        # increase the number of function evaluation counter
        iterations_number += 1

    # update the best antibody
    best_fitness, idx = min((s[1], i) for i, s in enumerate(population))
    best_antibody = population[idx][0]

    # update the end time
    end_time = time.time()
    duration = end_time - start_time
    # result display
    print('Running Time: %s Secounds' % duration)
    print("Best Fitness:", best_fitness)
    print("Best Antibody:", best_antibody)
    # get the best solution
    return best_antibody, best_fitness, duration, \
        iterations_number, iteration_results
