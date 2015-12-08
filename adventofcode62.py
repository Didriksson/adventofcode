import numpy as np
lights = np.zeros((1000,1000), dtype=np.int32)

def getRectangle(fromCoord, toCoord):
    coordinates = []
    currentPosition = [fromCoord[0], fromCoord[1]]
    while currentPosition[1] <= toCoord[1]:
        currentPosition[0] = fromCoord[0]
        while currentPosition[0] <= toCoord[0]:
            coordinates.append([currentPosition[0], currentPosition[1]])
            currentPosition[0] += 1
        currentPosition[1] += 1
    return coordinates

def turnOn(coordinates):
    for cord in coordinates:
        lights[cord[0]][cord[1]] += +1

def turnOff(coordinates):
    for cord in coordinates:
        if lights[cord[0]][cord[1]] > 0:
            lights[cord[0]][cord[1]] += -1

def toggle(coordinates):
    for cord in coordinates:
            lights[cord[0]][cord[1]] += 2


input = open('adventofcode61.txt', 'r')
inputLines = [line.strip() for line in input]
hanteradeAntalRader = 0
for line in inputLines:
    if hanteradeAntalRader % 10 == 0:
        print hanteradeAntalRader
    splitline = line.split(' ')
    toCoord = [int(x) for x in splitline.pop().split(',')]
    splitline.pop()
    fromCoord = [int(x) for x in splitline.pop().split(',')]
    command = ' '
    command = command.join(splitline)
    
    if command == 'toggle':
        toggle(getRectangle(fromCoord, toCoord))
    elif command == 'turn off':
        turnOff(getRectangle(fromCoord, toCoord))
    elif command == 'turn on':
        turnOn(getRectangle(fromCoord, toCoord))
    hanteradeAntalRader += 1

print lights.sum(dtype=np.int32)
