import os


def day1(part):
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    caloriesPerElf = [0]
    with open(os.path.join(__location__, 'input.txt')) as fp:
        for calories in fp:
            if calories.strip() == '':
                caloriesPerElf.append(0)
            else:
                caloriesPerElf[-1] += int(calories)
    caloriesPerElf.sort()


    match part:
        case 'part1':
            print(max(caloriesPerElf))
        case 'part2':
            print(sum(caloriesPerElf[-3:]))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    day1("part1")
    day1("part2")
