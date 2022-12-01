import os.path
from subprocess import call
from datetime import date

def run_current_advent_of_code_day():
    today = date.today().day
    d = os.path.dirname("C:/Users/olive/PycharmProjects/adventofcode2022/day" + str(today) + "/")
    call(["python", f"{d}/day" + str(today) + ".py"])



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_current_advent_of_code_day()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
