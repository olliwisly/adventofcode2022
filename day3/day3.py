import math
import os


def day3(part):
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
                length = len(line) // 2
                commonCharacters = ''.join(set(line[:length]).intersection(line[length:]))
                if commonCharacters.islower():
                    totalScore += ord(commonCharacters) - 96
                else:
                    totalScore += ord(commonCharacters) - 64 + 26
            print(totalScore)
        case 'part2':
            totalScore=0
            for i in range(len(inputData) // 3):

                commonCharacter = ''.join((set(inputData[i*3].replace("\n", "")).intersection(set(inputData[i*3+1].replace("\n", "")))).intersection(set(inputData[i*3+2].replace("\n", ""))))
                if commonCharacter.islower():
                    totalScore += ord(commonCharacter) - 96
                else:
                    totalScore += ord(commonCharacter) - 64 + 26
            print(totalScore)





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # day3("part1")
    day3("part2")
