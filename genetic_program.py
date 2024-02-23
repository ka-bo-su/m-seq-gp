import random
from time import sleep

class gp:
    def __init__(self):
        self.population = []
        self.fitness = []
        self.target = "Hello, World!"
        self.mutation_rate = 0.01
        self.mating_pool = []
        self.generations = 0
        self.finished = False
        self.perfect_score = 1
        self.num_of_population = 200
        self.bit_length = 18

    def random_gen(self):
        for i in range(self.num_of_population):
            random_data = []
            for j in range(len(self.bit_length)):
                random_data.append(chr(random.randint(0, 1)))
            self.population.append(random_data)

    def calc_fitness(self):
        for i in range(self.num_of_population):
            score = 0
            for j in range(self.bit_length):
                if self.population[i][j] == self.target[j]:
                    score += 1
            self.fitness.append(score / self.bit_length)


def gen_m_seq():
    primitive_poly = 0b1011100111101110011
    deg = primitive_poly.bit_length() - 1
    print(deg)
    print(primitive_poly, deg)
    m_seq_list = []
    a = 1
    for i in range(2**deg-1):
        a = a << 1
        if a >= 1<<deg:
            a = a ^ primitive_poly
        m_seq_list.append(bin(a)[-1:])
    return m_seq_list


def main():
    print("start")

if __name__ == "__main__":
    main()
    print(gen_m_seq())