import os
import pandas as pd
from io import StringIO
import re


def moveXFromTo(x, source, dest):

    for nb in range(0, x, 1):
        dest.insert(nb, source.pop(0))
    return source, dest


def getPops(docks):
    return "".join([l[0].replace("[", "").replace("]", "") for l in docks])


def findTopOfStacks(file: str):
    current_python_path = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(current_python_path, file)
    with open(filepath) as f:
        data = f.read()
        split_file = data.split("move")
        dock = split_file[0]
        orders_str = "".join(split_file[1:]).split("\n")
        docks = pd.read_csv(
            StringIO(dock.split("1")[0].replace("    ", " ")), sep=" ", header=None
        )
        docks = list(map(list, zip(*docks.values.tolist())))
        formated_docks = []
        for l in docks:
            sub_list = [e for e in l if str(e) != "nan"]
            if len(sub_list) > 0:
                formated_docks.append(sub_list)
        for order in orders_str:
            orders = [int(s) for s in re.findall(r"\b\d+\b", order)]
            src = formated_docks[orders[1] - 1]
            dest = formated_docks[orders[2] - 1]
            src, dest = moveXFromTo(orders[0], src, dest)
        return getPops(formated_docks)


if __name__ == "__main__":
    print(findTopOfStacks("data.csv"))
