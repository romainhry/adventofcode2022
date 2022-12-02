import os
import pandas as pd
def main():
    current_python_path = os.path.dirname(os.path.abspath(__file__))
    filepath=os.path.join(current_python_path,'data.csv')
    df = pd.read_csv(filepath, header=None, sep=" ")
    points = {"A":1, "B":2, "C":3}
    equivalence = {"X":"A", "Y":"B", "Z":"C"}
    strategy_point = 0
    for _, hand in df.iterrows():
        my_hand_points = points[equivalence[hand[1]]]
        oponent_point = points[hand[0]]
        if oponent_point == my_hand_points:
            strategy_point += 3
        elif oponent_point < my_hand_points:
            if my_hand_points - oponent_point == 1:
                strategy_point += 6
        else:
            if oponent_point - my_hand_points == 2:
                strategy_point += 6
        strategy_point += my_hand_points

    print(strategy_point)
        



if __name__ == "__main__":
    main()