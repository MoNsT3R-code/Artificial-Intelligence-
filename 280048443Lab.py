import random

POP_SIZE = 6
CHROM_LENGTH = 10
GENERATIONS = 10
MUTATION_RATE = 0.1

# Create random individual
def create_individual():
    individual = []
    for i in range(CHROM_LENGTH):
        individual.append(random.randint(0, 1))
    return individual

# Fitness = number of 1s
def fitness(individual):
    return sum(individual)

# Create initial population
def create_population():
    population = []
    for i in range(POP_SIZE):
        population.append(create_individual())
    return population

# Select best 2 parents
def select_parents(population):
    population.sort(key=fitness, reverse=True)
    return population[0], population[1]

# Crossover (single point)
def crossover(p1, p2):
    point = random.randint(1, CHROM_LENGTH - 1)
    child = p1[:point] + p2[point:]
    return child

# Mutation
def mutate(individual):
    for i in range(len(individual)):
        if random.random() < MUTATION_RATE:
            individual[i] = 1 - individual[i]
    return individual

# Main GA function
def genetic_algorithm():
    population = create_population()

    for gen in range(GENERATIONS):

        # Evaluate best
        best = max(population, key=fitness)
        print("Generation", gen, "Best:", best, "Fitness:", fitness(best))

        # Selection
        p1, p2 = select_parents(population)

        # Create new population
        new_population = []

        for i in range(POP_SIZE):
            child = crossover(p1, p2)
            child = mutate(child)
            new_population.append(child)

        population = new_population

# Run
genetic_algorithm()