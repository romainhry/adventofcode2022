import os
import pandas as pd
def main():
    current_python_path = os.path.dirname(os.path.abspath(__file__))
    filepath=os.path.join(current_python_path,'data.csv')
    offset_cap = ord("A") - 27
    offset_low = ord("a") - 1
    with open(filepath) as f:
        rucksack_list =f.readlines()
        result = 0
        for rucksack in rucksack_list:
            comp1=rucksack[slice(0,len(rucksack)//2)]
            comp2=rucksack[slice(len(rucksack)//2, len(rucksack))]
            for c in comp1:
                if c in comp2:
                    if c >="a":
                        result += ord(c) - offset_low
                    else:
                        result += ord(c) - offset_cap
                    break
    print(result)


if __name__ == "__main__":
    main()