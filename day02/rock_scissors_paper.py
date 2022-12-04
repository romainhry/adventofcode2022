import os
import pandas as pd


def main():
    current_python_path = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(current_python_path, "data.csv")
    df = pd.read_csv(filepath, header=None, sep=" ")
    draw_points = {"A": 1, "B": 2, "C": 3}
    win_points = {"A": 2, "B": 3, "C": 1}
    loose_points = {"A": 3, "B": 1, "C": 2}
    equivalence = {"X": "loose", "Y": "draw", "Z": "win"}
    strategy_point = 0
    for _, hand in df.iterrows():
        round_result = equivalence[hand[1]]
        if round_result == "win":
            strategy_point += win_points[hand[0]] + 6
        elif round_result == "draw":
            strategy_point += draw_points[hand[0]] + 3
        else:
            strategy_point += loose_points[hand[0]] + 0
    print(strategy_point)


if __name__ == "__main__":
    main()
