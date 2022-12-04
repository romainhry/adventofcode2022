import os


def main():
    NUMBER_OF_CARRYING_ELVES = 3
    current_python_path = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(current_python_path, "data.csv")
    with open(filepath) as f:
        data = f.read()
        elems = data.split("\n")
        max_elf_cal = [0] * NUMBER_OF_CARRYING_ELVES
        elf_cal = 0
        for cal in elems:
            if cal == "":
                third_elf_cal = min(max_elf_cal)
                if elf_cal > third_elf_cal:
                    max_elf_cal[max_elf_cal.index(third_elf_cal)] = elf_cal
                elf_cal = 0
                continue
            elf_cal = elf_cal + int(cal)
        print(sum(max_elf_cal))


if __name__ == "__main__":
    main()
