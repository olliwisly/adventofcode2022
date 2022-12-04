import os


def day4(part):
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    inputData = []
    with open(os.path.join(__location__, 'input.txt')) as fp:
        for line in fp:
            inputData.append(line)

    match part:
        case 'part1':
            totalScore=0
            for line in inputData:
                elvepair = line.replace("\n", "").split(',')
                elve1 = elvepair[0].split('-')
                elve2 = elvepair[1].split('-')
                if (int(elve2[0]) <= int(elve1[0]) and int(elve1[1]) <= int(elve2[1])) or (
                        int(elve1[0]) <= int(elve2[0]) and int(elve2[1]) <= int(elve1[1])):
                    totalScore +=1
            print(totalScore)
        case 'part2':
            totalScore=0
            for line in inputData:
                elvepair = line.replace("\n", "").split(',')
                elve1 = elvepair[0].split('-')
                elve2 = elvepair[1].split('-')
                if (int(elve2[0]) <= int(elve1[0]) <= int(elve2[1])) or (
                        int(elve1[0]) <= int(elve2[0]) <= int(elve1[1])):
                    totalScore += 1
            print(totalScore)





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    day4("part1")
    day4("part2")
