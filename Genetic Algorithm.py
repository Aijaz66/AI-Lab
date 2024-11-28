import random

def fitness(individual):
    return sum(individual)

def create_population(population_size, individual_length):
    population = []
    for _ in range(population_size):
        individual = []
        for _ in range(individual_length):
            individual.append(random.randint(0, 1))
        population.append(individual)
    return population

def select_parents(population):
    fitness_scores = []
    for ind in population:
        fitness_scores.append(fitness(ind))

    total_fitness = sum(fitness_scores)
    probabilities = []
    for score in fitness_scores:
        probabilities.append(score / total_fitness)

    parent1 = random.choices(population, weights=probabilities, k=1)[0]
    parent2 = random.choices(population, weights=probabilities, k=1)[0]

    return parent1, parent2

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

def mutate(individual, mutation_rate):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = 1 - individual[i]

def genetic_algorithm(population_size, individual_length, generations, mutation_rate):
    population = create_population(population_size, individual_length)
    overall_best = max(population, key=fitness)

    for generation in range(1, generations + 1):
        new_population = []
        for _ in range(population_size):
            parent1, parent2 = select_parents(population)
            child = crossover(parent1, parent2)
            mutate(child, mutation_rate)
            new_population.append(child)
        population = new_population

        current_best = max(population, key=fitness)
        if fitness(current_best) > fitness(overall_best):
            overall_best = current_best

        print(f"Generation {generation}: Best Individual = {current_best}, Fitness = {fitness(current_best)}")

    return overall_best


final_result = genetic_algorithm(population_size=10, individual_length=8, generations=20, mutation_rate=0.01)
print("Final Best Individual:", final_result)
print("Final Fitness:", fitness(final_result))
