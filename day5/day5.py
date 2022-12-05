import os

def day5(part):
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    inputData = []
    with open(os.path.join(__location__, 'input.txt')) as fp:
        for line in fp:
            inputData.append(line)

    currentLocations=[[] for i in range(9)]
    for rows in range(8):
        for columns in range(9):
            nextInput = inputData[7-rows][columns*4+1]
            if nextInput != ' ':
                currentLocations[columns].append(nextInput)

    match part:
        case 'part1':
            for line in inputData[10:]:
                splitline = line.replace("\n", "").split(' ')
                changenumber = int(splitline[1])
                fromline = int(splitline[3])-1
                toline = int(splitline[5])-1
                for i in range(changenumber):
                    currentLocations[toline].append(currentLocations[fromline].pop(-1))
            finaltopstrings=''
            for location in range(9):
                finaltopstrings += currentLocations[location][-1]
            print(finaltopstrings)
        case 'part2':
            for line in inputData[10:]:
                splitline = line.replace("\n", "").split(' ')
                changenumber = int(splitline[1])
                fromline = int(splitline[3]) - 1
                toline = int(splitline[5]) - 1
                for i in range(-changenumber, 0):
                    currentLocations[toline].append(currentLocations[fromline].pop(i))
            finaltopstrings = ''
            for location in range(9):
                finaltopstrings += currentLocations[location][-1]
            print(finaltopstrings)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    day5("part1")
    day5("part2")
