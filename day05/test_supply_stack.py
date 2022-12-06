from day05 import supply_stack


def test_findTopOfStacks_dataReturnsCMZ():
    assert supply_stack.findTopOfStacks("test_data.csv") == "MCD"
