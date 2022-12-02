import os

def day2(part):
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    totalScore = 0
    with open(os.path.join(__location__, 'input.txt')) as fp:
        for game in fp:
            match game.strip():
                case 'A X':
                    totalScore += 4
                case 'A Y':
                    totalScore += 8
                case 'A Z':
                    totalScore += 3
                case 'B X':
                    totalScore += 1
                case 'B Y':
                    totalScore += 5
                case 'B Z':
                    totalScore += 9
                case 'C X':
                    totalScore += 7
                case 'C Y':
                    totalScore += 2
                case 'C Z':
                    totalScore += 6

    totalScore2 = 0
    with open(os.path.join(__location__, 'input.txt')) as fp:
        for game in fp:
            match game.strip():
                case 'A X':
                    totalScore2 += 3
                case 'A Y':
                    totalScore2 += 4
                case 'A Z':
                    totalScore2 += 8
                case 'B X':
                    totalScore2 += 1
                case 'B Y':
                    totalScore2 += 5
                case 'B Z':
                    totalScore2 += 9
                case 'C X':
                    totalScore2 += 2
                case 'C Y':
                    totalScore2 += 6
                case 'C Z':
                    totalScore2 += 7

    match part:
        case 'part1':
            print(totalScore)
        case 'part2':
             print(totalScore2)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    day2("part1")
    day2("part2")