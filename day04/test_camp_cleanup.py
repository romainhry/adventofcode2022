from day04 import camp_cleanup


def test_findOverlappingPairNumber_testDataReturns2():
    assert camp_cleanup.findOverlappingPairNumber("test_data.csv") == [2, 4]


def test_findOverlappingPairNumber_dataReturns528():
    assert camp_cleanup.findOverlappingPairNumber("data.csv") == [528, 881]
