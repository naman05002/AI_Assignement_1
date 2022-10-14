from audioop import cross
from collections import defaultdict
from Graph_Creator import *
import random
import collections
import time 
import matplotlib.pyplot as plt
import numpy as np
no_of_edges = 200
no_of_nodes = 50
size_of_population = 500
population = list()

def main():
    gc = Graph_Creator()

#    ********* You can use the following two functions in your program

    edges = gc.CreateGraphWithRandomEdges(no_of_edges) # Creates a random graph with 50 vertices and 200 edges

    #Graph created from the edges
    graphCreator(edges)

    #Initial population initialized with random colors alloted to each node
    createInitPopulation(graph)


    print('Roll No: 2020A7PS0103G')
    print('Number of edges: ',no_of_edges)
    no_of_generations=50
    timeout = time.time() + 10
    fitnessploty = list()
    fitnessplotx = list()
    tim = time.time();
    deq = collections.deque();
    y= no_of_edges/5
    counter = 1
    while True:
        va = genetic_algorithm()
        fitnessploty.append(va[1])
        fitnessplotx.append(counter)
        counter+=1
        if(va[1]==50):
            break;

        if time.time() > timeout:
            break
        no_of_generations-=1

        if(y>0):
            deq.append(va[1])
            y-=1

        if(y==0):
            deq.append(va[1])
            deq.popleft()
            tempvar = deq[0]
            tempbool = True
            for element in deq:
                if(element!=tempvar):
                    tempbool=False
            if(tempbool==True):
                break
    answer = genetic_algorithm()
    answerdict = dict()

    for i in range(0,len(answer[0])):
        # print(answer[0][i])
        if answer[0][i]==0:
            answerdict[i]="G"
        if answer[0][i]==1:
            answerdict[i]="R"
        if answer[0][i]==2:
            answerdict[i]="B"
    timtimtim = time.time()-tim


    print('Best State:  \n',answerdict)
    print('Fitness value of best state: ',answer[1])
    print('Time taken: ',end="")
    print("{0:.2f}".format(timtimtim),end="")
    print(' seconds')

    xpoints = np.array(fitnessplotx)
    ypoints = np.array(fitnessploty)
    plt.plot(xpoints,ypoints)
    plt.xlabel("Number of Generations")
    plt.ylabel("Fitness Value")
    plt.show()

graph = defaultdict(list)


def addEdge(graph,u,v):
    graph[u].append(v)
    graph[v].append(u)

def graphCreator(edges):
    for val in edges: 
        addEdge(graph,val[0],val[1])

def fitness(graph):
    fit = list()
    for chromosome in population: 
        fitnum = fitnessofChromosome(graph,chromosome)
        fit.append(fitnum)
    return fit

def fitnessofChromosome(graph,chromosome):
    fit = 0
    for val in graph:
        num = chromosome[val] #current color val
        ff = True
        for adj in graph[val]:
            if(chromosome[adj]==num):

                ff = False
        if(ff==True):
            fit+=1
    return fit



def mutation(chromosome):
    for i in range(len(chromosome)):
        if(random.randint(0,500) == 0):
            chromosome[i] = random.randint(0,2)
    return chromosome
def weighted_random_choices(fitness):
    parentlist = random.choices(population,weights=fitness,k=2)
    return parentlist

def reproduce(parentlist):
    parent1 = parentlist[0]
    parent2 = parentlist[1]
    n = len(parent1)
    crossover = random.randint(1,n-1)
    p11 = parent1[0:crossover]
    p21 = parent2[0:crossover]
    p12 = parent1[crossover:n]
    p22 = parent2[crossover:n]
    child1 = list()
    child2 = list()
    for i in p11:
        child1.append(i)
    for i in p22:
        child1.append(i)
    for i in p21:
        child2.append(i)
    for i in p12:
        child2.append(i)

    return [child1,child2]

def sort_list(list1, list2):
    zipped_pairs = zip(list2, list1)
    z = [x for _, x in sorted(zipped_pairs)]
    return z

def genetic_algorithm():
    weights = fitness(graph)
    population2 = []
    global population
    #elitism begins
    elitism_ratio = 0.2
    pop = sort_list(population,weights)
    population = pop
    weights.sort()

    numberOfElite = int(elitism_ratio*len(population))

    for i in range(0,numberOfElite):
        population2.append(population.pop())
        weights.pop()
    #elitism ends

    #culling begins
    average = sum(weights)/len(weights)
    cullinglist = []
    cullingweight = []
    for i in range (len(population)):
        if(weights[i] > average):
            cullinglist.append(population[i])
            cullingweight.append(weights[i])

    #culling ends
    population = cullinglist
    weights = cullingweight
    for i in range(0,len(population)):
        parentlist = weighted_random_choices(weights)
        childlist = reproduce(parentlist)
        childlist[0] = mutation(childlist[0])
        childlist[1] = mutation(childlist[1])
        if(fitnessofChromosome(graph,childlist[0])>fitnessofChromosome(graph,childlist[1])):
            population2.append(childlist[0])
        else:
            population2.append(childlist[1])    
    # global population
    population =  population2
    fitnesscurrent = fitness(graph)
    max=0
    ansi = []
    for i in range (len(fitnesscurrent)):
        if fitnesscurrent[i]>max:
            max=fitnesscurrent[i]
            ansi=population[i]
    return [ansi,max]
def createInitPopulation(graph):
    for i in range(0,size_of_population):
        chromosome = list()
        for i in range(0,no_of_nodes):
            n = random.randint(0,2)
            chromosome.append(n)
        # print(chromosome)
        population.append(chromosome)

if __name__=='__main__':
    main()