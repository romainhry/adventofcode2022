import os

def computePriority(item):
    offset_cap = ord("A") - 27
    offset_low = ord("a") - 1
    if item >="a":
        return ord(item) - offset_low
    else:
        return ord(item) - offset_cap

def computePriorityInItemGroup(items):
    for item in items[0]:
        is_common = True
        for items_to_check in items[1:]:
            if item not in items_to_check:
                is_common = False
                break
        if is_common:
            return computePriority(item)
    
def getConpartimentsFrom(rucksack: str):
    comp1=rucksack[slice(0,len(rucksack)//2)]
    comp2=rucksack[slice(len(rucksack)//2, len(rucksack))]
    return [comp1,comp2]


def main():
    current_python_path = os.path.dirname(os.path.abspath(__file__))
    filepath=os.path.join(current_python_path,'data.csv')

    NUMBER_MEMBER_PER_GROUP = 3
    with open(filepath) as f:
        rucksack_list =f.readlines()
        priotities_badge = 0
        item_prio = 0
        member_count =0
        group_rucksack = []
        for rucksack in rucksack_list:
            group_rucksack.append(rucksack)
            member_count +=1
            if member_count == NUMBER_MEMBER_PER_GROUP:
                priotities_badge += computePriorityInItemGroup(group_rucksack)
                member_count =0
                group_rucksack = []     

            item_prio += computePriorityInItemGroup(getConpartimentsFrom(rucksack))
        print(item_prio)
        print(priotities_badge)



if __name__ == "__main__":
    main()