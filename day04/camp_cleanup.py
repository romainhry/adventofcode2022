import os


def isSectionsInPartnerSection(section, partner_section):
    if (
        int(section[0]) >= int(partner_section[0])
        and int(section[0]) <= int(partner_section[1])
        and int(section[1]) <= int(partner_section[1])
        and int(section[1]) >= int(partner_section[0])
    ):
        return True
    return False


def findOverlappingPairNumber(file: str):
    current_python_path = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(current_python_path, file)
    with open(filepath) as f:
        overlappingPairResult = 0
        for pair in f.readlines():
            elf_sections = pair.split(",")
            elf_bounds = elf_sections[0].split("-")
            partner_bounds = elf_sections[1].split("-")
            if isSectionsInPartnerSection(
                elf_bounds, partner_bounds
            ) or isSectionsInPartnerSection(partner_bounds, elf_bounds):
                overlappingPairResult += 1
    return overlappingPairResult


if __name__ == "__main__":
    print(findOverlappingPairNumber("data.csv"))
