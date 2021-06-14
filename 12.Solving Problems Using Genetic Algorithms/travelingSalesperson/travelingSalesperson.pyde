import random

class City:
    def __init__(self, x, y,num): # initialzes a city to have a unique x, y, and number associated with it
        self.x = x
        self.y = y
        self.number = num
        self.radius = 5
    
    def display(self):
        fill(0,255,255) # sky blue
        ellipse(self.x,self.y,self.radius*2,self.radius*2)

        textSize(20)
        text(self.number, self.x-self.radius, self.y-self.radius*2) # displays information about each city above the point
        noFill()

class Route:
    def __init__(self,numCities):
        self.distance = 0 # measures the total distance, starting from the first city to the next to the end
        # puts city numbers into a random order 
        # random.sample() accepts a list and a number denoting how many times to randomly select from the list
        self.cityNums = random.sample(list(range(numCities)), numCities)
        # this is going to be the most important part of the path-finder algorithm because random.sample() will return a random list that we will check over and over again to calculate the distances
    
    def display(self,cities): # displays the route
        strokeWeight(3)
        stroke(255,0,255) # purple
        beginShape()
        for i in self.cityNums:
            vertex(cities[i].x, cities[i].y)
            cities[i].display()
        endShape(CLOSE)
    
    def calcLength(self): # returns the total distance of the route depending on the city list
        self.distance = 0 # resets the distance parameter

        for i, num in enumerate(self.cityNums): # i is increnting, num is the actually city number
            self.distance += dist(cities[num].x, cities[num].y, cities[self.cityNums[i-1]].x, cities[self.cityNums[i-1]].y)
            # the reason we do cities[num] vs self.numCities is because cities[num] will track the current city, since the list won't be in sequential order
            # self.numCities[i-1] is needed because this tracks the previous location based on the random list, not sequentially which city was previous
        return self.distance
    
    def mutateN(self,num,cities,numCities):
        indices = random.sample(list(range(numCities)), num) # randomly picks new indices
        child = Route(numCities)
        child.cityNums = self.cityNums[::] # inherits the parent Route's city numbers

        for i in range(num - 1): # range(num-1) or else we would swap every number back to its original location
            child.cityNums[indices[i]], child.cityNums[indices[(i+1) % num]] = child.cityNums[indices[(i+1) % num]], child.cityNums[indices[i]] # swaps one random index with the very next one
        return child
    
    def crossover(self,partner,numCities):
        child = Route(numCities)
        # randomly chooses slice point
        index = random.randint(1, numCities - 2)
        child.cityNums = self.cityNums[:index] # inherits numbers from the callee parent

        if random.random() < 0.5: # half the time, the numbers will the reversed
            child.cityNums = child.cityNums[::-1]

        notinslice = [x for x in partner.cityNums if x not in child.cityNums] # populates notinslice with numbers that are not the child.cityNums, but are in parter.cityNums
        child.cityNums += notinSlice
        return child


cities = []
N_CITIES = 100 
random_improvements = 0
mutated_improvements = 0
population = []
POP_N = 1000 # number of routes
frame = 0

def setup():
    global best, record_distance, first, population
    size(600,600)

    for i in range(N_CITIES):
        # appends cities with random locations to the list
        cities.append(City(random.randint(50,width-50), random.randint(50,height-50), i))
        # 50 means 50 units away from the borders on the window
    for i in range(POP_N):
        population.append(Route(N_CITIES))
    best = Route(N_CITIES) # initializes the 'best' Route
    record_distance = best.calcLength() # calculates the total distance based on the random initial condition
    first = record_distance

def draw():
    global best, record_distance, random_improvements, mutated_improvements, population, frame
    background(0)

    best.display(cities) # displays the best route 
    # println("Random : " + str(random_improvements))
    # println("Mutated: " + str(mutated_improvements))

    # route1 = Route(N_CITIES)
    # length1 = route1.calcLength()

    population.sort(key=Route.calcLength) # sorts the population list, which is dependent on the calcLength() method
    population = population[:POP_N] # limits the size of the population
    length1 = population[0].calcLength()

    # if length1 < record_distance:
        # record_distance = length1
        # best = route1
        # random_improvements += 1

    if length1 < record_distance:
        record_distance = length1
        println(record_distance)
        best = population[0]

    # for i in range(0, 5): # tells the program to mutate indices 2-6 in the number list, then check the results
    # # it turns out the mutating (swapping around pairs of indices) is much more effective than randomly choosing the route
        # mutated = Route(N_CITIES)
        # mutated.cityNums = best.cityNums[::]
        # mutated = mutated.mutateN(i, cities, N_CITIES)
        # length2 = mutated.calcLength()
        # if length2 < record_distance:
            # record_distance = length2
 
        # if length2 < record_distance:
            # record_distance = length2
            # best = mutated
            # mutated_improvements += 1

    for i in range(3,25): # mutates the best in the population
        if i < N_CITIES:
            new = best.mutateN(i,cities,N_CITIES)
            population.append(new)

    for i in range(3,25): # mutates random routes in the population
        if i < N_CITIES:
            new = random.choice(population)
            new = new.mutateN(i,cities,N_CITIES)
            population.append(new)

    # save('frames/traveling + ' + str(frame) + '.jpg')
    # frame += 1
    # if frame == 300:
        # exit()
