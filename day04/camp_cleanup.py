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


def isSectionsPartlyInPartnerSection(section, partner_section):
    if (
        int(section[0]) >= int(partner_section[0])
        and int(section[0]) <= int(partner_section[1])
    ) or (
        int(section[1]) <= int(partner_section[1])
        and int(section[1]) >= int(partner_section[0])
    ):
        return True
    return False


def findOverlappingPairNumber(file: str):
    current_python_path = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(current_python_path, file)
    with open(filepath) as f:
        fullOverlappingPairResult = 0
        partlyOverlappingPairResult = 0
        for pair in f.readlines():
            elf_sections = pair.split(",")
            elf_bounds = elf_sections[0].split("-")
            partner_bounds = elf_sections[1].split("-")
            if isSectionsInPartnerSection(
                elf_bounds, partner_bounds
            ) or isSectionsInPartnerSection(partner_bounds, elf_bounds):
                fullOverlappingPairResult += 1
            if isSectionsPartlyInPartnerSection(
                elf_bounds, partner_bounds
            ) or isSectionsPartlyInPartnerSection(partner_bounds, elf_bounds):
                partlyOverlappingPairResult += 1
    return [fullOverlappingPairResult, partlyOverlappingPairResult]


if __name__ == "__main__":
    print(findOverlappingPairNumber("data.csv"))
