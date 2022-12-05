from day05 import supply_stack


def test_findTopOfStacks_dataReturnsCMZ():
    assert supply_stack.findTopOfStacks("test_data.csv") == "CMZ"


# def test_findTopOfStacks_dataReturnsCMZ():
#    assert supply_stack.findTopOfStacks("data.csv") == [528, 881]
