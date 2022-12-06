import os

def day6(part):
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    inputData = []
    with open(os.path.join(__location__, 'input.txt')) as fp:
        for line in fp:
            inputData.append(line)



    match part:
        case 'part1':
            currentLocation = 0
            while currentLocation < len(inputData[0]) - 3:
                currentpart = inputData[0][currentLocation:currentLocation + 4]
                if (len(set(currentpart)) == 4):
                    print(currentLocation + 4)
                    break
                currentLocation += 1
        case 'part2':
            currentLocation = 0
            while currentLocation < len(inputData[0]) - 14:
                currentpart = inputData[0][currentLocation:currentLocation + 14]
                if (len(set(currentpart)) == 14):
                    print(currentLocation + 14)
                    break
                currentLocation += 1

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    day6("part1")
    day6("part2")
